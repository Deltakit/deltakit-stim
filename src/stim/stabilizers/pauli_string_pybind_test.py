# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import itertools
import numpy as np
import lestim
import pytest


def test_identity():
    p = lestim.PauliString(3)
    assert len(p) == 3
    assert p[0] == p[1] == p[2] == 0
    assert p.sign == +1


def test_from_str():
    p = lestim.PauliString("-_XYZ_ZYX")
    assert len(p) == 8
    assert p[0] == 0
    assert p[1] == 1
    assert p[2] == 2
    assert p[3] == 3
    assert p[4] == 0
    assert p[5] == 3
    assert p[6] == 2
    assert p[7] == 1
    assert p.sign == -1

    p = lestim.PauliString("")
    assert len(p) == 0
    assert p.sign == +1

    p = lestim.PauliString("X")
    assert len(p) == 1
    assert p[0] == 1
    assert p.sign == +1

    p = lestim.PauliString("+X")
    assert len(p) == 1
    assert p[0] == 1
    assert p.sign == +1

    p = lestim.PauliString("iX")
    assert len(p) == 1
    assert p[0] == 1
    assert p.sign == 1j

    p = lestim.PauliString("+iX")
    assert len(p) == 1
    assert p[0] == 1
    assert p.sign == 1j

    p = lestim.PauliString("-iX")
    assert len(p) == 1
    assert p[0] == 1
    assert p.sign == -1j

    assert lestim.PauliString("X5*Y10") == lestim.PauliString("_____X____Y")
    assert lestim.PauliString("X5*Y5") == lestim.PauliString("iZ5")


def test_equality():
    assert not (lestim.PauliString(4) == None)
    assert not (lestim.PauliString(4) == "other object")
    assert not (lestim.PauliString(4) == object())
    assert lestim.PauliString(4) != None
    assert lestim.PauliString(4) != "other object"
    assert lestim.PauliString(4) != object()

    assert lestim.PauliString(4) == lestim.PauliString(4)
    assert lestim.PauliString(3) != lestim.PauliString(4)
    assert not (lestim.PauliString(4) != lestim.PauliString(4))
    assert not (lestim.PauliString(3) == lestim.PauliString(4))

    assert lestim.PauliString("+X") == lestim.PauliString("+X")
    assert lestim.PauliString("+X") != lestim.PauliString("-X")
    assert lestim.PauliString("+X") != lestim.PauliString("+Y")
    assert lestim.PauliString("+X") != lestim.PauliString("-Y")
    assert lestim.PauliString("+X") != lestim.PauliString("+iX")
    assert lestim.PauliString("+X") != lestim.PauliString("-iX")

    assert lestim.PauliString("__") != lestim.PauliString("_X")
    assert lestim.PauliString("__") != lestim.PauliString("X_")
    assert lestim.PauliString("__") != lestim.PauliString("XX")
    assert lestim.PauliString("__") == lestim.PauliString("__")


def test_random():
    p1 = lestim.PauliString.random(100)
    p2 = lestim.PauliString.random(100)
    assert p1 != p2

    seen_signs = {lestim.PauliString.random(1).sign for _ in range(200)}
    assert seen_signs == {1, -1}

    seen_signs = {lestim.PauliString.random(1, allow_imaginary=True).sign for _ in range(200)}
    assert seen_signs == {1, -1, 1j, -1j}


def test_str():
    assert str(lestim.PauliString(3)) == "+___"
    assert str(lestim.PauliString("XYZ")) == "+XYZ"
    assert str(lestim.PauliString("-XYZ")) == "-XYZ"
    assert str(lestim.PauliString("iXYZ")) == "+iXYZ"
    assert str(lestim.PauliString("-iXYZ")) == "-iXYZ"


def test_repr():
    assert repr(lestim.PauliString(3)) == 'stim.PauliString("+___")'
    assert repr(lestim.PauliString("-XYZ")) == 'stim.PauliString("-XYZ")'
    vs = [
        lestim.PauliString(""),
        lestim.PauliString("ZXYZZ"),
        lestim.PauliString("-XYZ"),
        lestim.PauliString("I"),
        lestim.PauliString("iIXYZ"),
        lestim.PauliString("-iIXYZ"),
    ]
    for v in vs:
        r = repr(v)
        assert eval(r, {'stim': lestim}) == v

def test_to_tableau():
    p = lestim.PauliString("XZ_Y")
    t = p.to_tableau()
    assert t.x_output(0) == lestim.PauliString("+X___")
    assert t.x_output(1) == lestim.PauliString("-_X__")
    assert t.x_output(2) == lestim.PauliString("+__X_")
    assert t.x_output(3) == lestim.PauliString("-___X")
    assert t.z_output(0) == lestim.PauliString("-Z___")
    assert t.z_output(1) == lestim.PauliString("+_Z__")
    assert t.z_output(2) == lestim.PauliString("+__Z_")
    assert t.z_output(3) == lestim.PauliString("-___Z")

    p_random = lestim.PauliString.random(32)
    p_random.sign = 1
    p_random_roundtrip = p_random.to_tableau().to_pauli_string()
    assert p_random == p_random_roundtrip

def test_commutes():
    def c(a: str, b: str) -> bool:
        return lestim.PauliString(a).commutes(lestim.PauliString(b))

    assert c("", "")
    assert c("X", "_")
    assert c("X", "X")
    assert not c("X", "Y")
    assert not c("X", "Z")

    assert c("XXXX", "YYYY")
    assert c("XXXX", "YYYZ")
    assert not c("XXXX", "XXXZ")
    assert not c("XXXX", "___Z")
    assert not c("XXXX", "Z___")
    assert c("XXXX", "Z_Z_")


def test_product():
    assert lestim.PauliString("") * lestim.PauliString("") == lestim.PauliString("")
    assert lestim.PauliString("i") * lestim.PauliString("i") == lestim.PauliString("-")
    assert lestim.PauliString("i") * lestim.PauliString("-i") == lestim.PauliString("+")
    assert lestim.PauliString("-i") * lestim.PauliString("-i") == lestim.PauliString("-")
    assert lestim.PauliString("i") * lestim.PauliString("-") == lestim.PauliString("-i")

    x = lestim.PauliString("X")
    y = lestim.PauliString("Y")
    z = lestim.PauliString("Z")

    assert x == +1 * x == x * +1 == +x
    assert x * -1 == -x == -1 * x
    assert (-x)[0] == 1
    assert (-x).sign == -1
    assert -(-x) == x

    assert lestim.PauliString(10) * lestim.PauliString(11) == lestim.PauliString(11)

    assert x * z == lestim.PauliString("-iY")
    assert x * x == lestim.PauliString(1)
    assert x * y == lestim.PauliString("iZ")
    assert y * x == lestim.PauliString("-iZ")
    assert x * y == 1j * z
    assert y * x == z * -1j
    assert x.extended_product(y) == (1, 1j * z)
    assert y.extended_product(x) == (1, -1j * z)
    assert x.extended_product(x) == (1, lestim.PauliString(1))

    xx = lestim.PauliString("+XX")
    yy = lestim.PauliString("+YY")
    zz = lestim.PauliString("+ZZ")
    assert xx * zz == -yy
    assert xx.extended_product(zz) == (1, -yy)


def test_inplace_product():
    p = lestim.PauliString("X")
    alias = p

    p *= 1j
    assert alias == lestim.PauliString("iX")
    assert alias is p
    p *= 1j
    assert alias == lestim.PauliString("-X")
    p *= 1j
    assert alias == lestim.PauliString("-iX")
    p *= 1j
    assert alias == lestim.PauliString("+X")

    p *= lestim.PauliString("Z")
    assert alias == lestim.PauliString("-iY")

    p *= -1j
    assert alias == lestim.PauliString("-Y")
    p *= -1j
    assert alias == lestim.PauliString("iY")
    p *= -1j
    assert alias == lestim.PauliString("+Y")
    p *= -1j
    assert alias == lestim.PauliString("-iY")

    p *= lestim.PauliString("i_")
    assert alias == lestim.PauliString("+Y")
    p *= lestim.PauliString("i_")
    assert alias == lestim.PauliString("iY")
    p *= lestim.PauliString("i_")
    assert alias == lestim.PauliString("-Y")
    p *= lestim.PauliString("i_")
    assert alias == lestim.PauliString("-iY")

    p *= lestim.PauliString("-i_")
    assert alias == lestim.PauliString("-Y")
    p *= lestim.PauliString("-i_")
    assert alias == lestim.PauliString("iY")
    p *= lestim.PauliString("-i_")
    assert alias == lestim.PauliString("+Y")
    p *= lestim.PauliString("-i_")
    assert alias == lestim.PauliString("-iY")

    assert alias is p


def test_imaginary_phase():
    p = lestim.PauliString("IXYZ")
    ip = lestim.PauliString("iIXYZ")
    assert 1j * p == p * 1j == ip == -lestim.PauliString("-iIXYZ")
    assert p.sign == 1
    assert (-p).sign == -1
    assert ip.sign == 1j
    assert (-ip).sign == -1j
    assert lestim.PauliString("X") * lestim.PauliString("Y") == 1j * lestim.PauliString("Z")
    assert lestim.PauliString("Y") * lestim.PauliString("X") == -1j * lestim.PauliString("Z")


def test_get_set_sign():
    p = lestim.PauliString(2)
    assert p.sign == +1
    p.sign = -1
    assert str(p) == "-__"
    assert p.sign == -1
    p.sign = +1
    assert str(p) == "+__"
    assert p.sign == +1
    with pytest.raises(ValueError, match="new_sign"):
        p.sign = 5

    p.sign = 1j
    assert str(p) == "+i__"
    assert p.sign == 1j

    p.sign = -1j
    assert str(p) == "-i__"
    assert p.sign == -1j


def test_get_set_item():
    p = lestim.PauliString(5)
    assert list(p) == [0, 0, 0, 0, 0]
    assert p[0] == 0
    p[0] = 1
    assert p[0] == 1
    p[0] = 'Y'
    assert p[0] == 2
    p[0] = 'Z'
    assert p[0] == 3

    with pytest.raises(IndexError, match="new_pauli"):
        p[0] = 't'
    with pytest.raises(IndexError, match="new_pauli"):
        p[0] = 10

    assert p[1] == 0
    p[1] = 2
    assert p[1] == 2


def test_get_slice():
    p = lestim.PauliString("XXXX__YYYY__ZZZZX")
    assert p[:7] == lestim.PauliString("XXXX__Y")
    assert p[:-3] == lestim.PauliString("XXXX__YYYY__ZZ")
    assert p[::2] == lestim.PauliString("XX_YY_ZZX")
    assert p[::-1] == lestim.PauliString("XZZZZ__YYYY__XXXX")
    assert p[-3:3] == lestim.PauliString("")
    assert p[-6:-1] == lestim.PauliString("_ZZZZ")
    assert p[3:5:-1] == lestim.PauliString("")
    assert p[5:3:-1] == lestim.PauliString("__")
    assert p[4:2:-1] == lestim.PauliString("_X")
    assert p[2:0:-1] == lestim.PauliString("XX")


def test_copy():
    p = lestim.PauliString(3)
    p2 = p.copy()
    assert p == p2
    assert p is not p2

    p = lestim.PauliString("-i_XYZ")
    p2 = p.copy()
    assert p == p2
    assert p is not p2


def test_hash():
    # lestim.PauliString is mutable. It must not also be value-hashable.
    # Defining __hash__ requires defining a FrozenPauliString variant instead.
    with pytest.raises(TypeError, match="unhashable"):
        _ = hash(lestim.PauliString(1))


def test_add():
    ps = lestim.PauliString
    assert ps(0) + ps(0) == ps(0)
    assert ps(3) + ps(1000) == ps(1003)
    assert ps(1000) + ps(3) == ps(1003)
    assert ps("_XYZ") + ps("_ZZZ_") == ps("_XYZ_ZZZ_")

    p = ps("_XYZ")
    p += p
    assert p == ps("_XYZ_XYZ")
    for k in range(1, 8):
        p += p
        assert p == ps("_XYZ_XYZ" * 2**k)

    p = ps("_XXX")
    p += ps("Y")
    assert p == ps("_XXXY")

    p = ps("")
    alias = p
    p += ps("X")
    assert alias is p
    assert alias == ps("X")
    p += p
    assert alias is p
    assert alias == ps("XX")


def test_mul_different_sizes():
    ps = lestim.PauliString
    assert ps("") * ps("X" * 1000) == ps("X" * 1000)
    assert ps("X" * 1000) * ps("") == ps("X" * 1000)
    assert ps("Z" * 1000) * ps("") == ps("Z" * 1000)

    p = ps("Z")
    alias = p
    p *= ps("ZZZ")
    assert p == ps("_ZZ")
    p *= ps("Z")
    assert p == ps("ZZZ")
    assert alias is p


def test_div():
    assert lestim.PauliString("+XYZ") / +1 == lestim.PauliString("+XYZ")
    assert lestim.PauliString("+XYZ") / -1 == lestim.PauliString("-XYZ")
    assert lestim.PauliString("+XYZ") / 1j == lestim.PauliString("-iXYZ")
    assert lestim.PauliString("+XYZ") / -1j == lestim.PauliString("iXYZ")
    assert lestim.PauliString("iXYZ") / 1j == lestim.PauliString("XYZ")
    p = lestim.PauliString("__")
    alias = p
    assert p / -1 == lestim.PauliString("-__")
    assert alias == lestim.PauliString("__")
    p /= -1
    assert alias == lestim.PauliString("-__")
    p /= 1j
    assert alias == lestim.PauliString("i__")
    p /= 1j
    assert alias == lestim.PauliString("__")
    p /= -1j
    assert alias == lestim.PauliString("i__")
    p /= 1
    assert alias == lestim.PauliString("i__")


def test_mul_repeat():
    ps = lestim.PauliString
    assert ps("") * 100 == ps("")
    assert ps("X") * 100 == ps("X" * 100)
    assert ps("XYZ_") * 1000 == ps("XYZ_" * 1000)
    assert ps("XYZ_") * 1 == ps("XYZ_")
    assert ps("XYZ_") * 0 == ps("")

    assert 100 * ps("") == ps("")
    assert 100 * ps("X") == ps("X" * 100)
    assert 1000 * ps("XYZ_") == ps("XYZ_" * 1000)
    assert 1 * ps("XYZ_") == ps("XYZ_")
    assert 0 * ps("XYZ_") == ps("")

    assert ps("i") * 0 == ps("+")
    assert ps("i") * 1 == ps("i")
    assert ps("i") * 2 == ps("-")
    assert ps("i") * 3 == ps("-i")
    assert ps("i") * 4 == ps("+")
    assert ps("i") * 5 == ps("i")

    assert ps("-i") * 0 == ps("+")
    assert ps("-i") * 1 == ps("-i")
    assert ps("-i") * 2 == ps("-")
    assert ps("-i") * 3 == ps("i")
    assert ps("-i") * 4 == ps("+")
    assert ps("-i") * 5 == ps("-i")

    assert ps("-") * 0 == ps("+")
    assert ps("-") * 1 == ps("-")
    assert ps("-") * 2 == ps("+")
    assert ps("-") * 3 == ps("-")
    assert ps("-") * 4 == ps("+")
    assert ps("-") * 5 == ps("-")

    p = ps("XYZ")
    alias = p
    p *= 1000
    assert p == ps("XYZ" * 1000)
    assert alias is p


def test_init_list():
    assert lestim.PauliString([]) == lestim.PauliString(0)
    assert lestim.PauliString([0, 1, 2, 3]) == lestim.PauliString("_XYZ")

    with pytest.raises(ValueError, match="pauli"):
        _ = lestim.PauliString([-1])
    with pytest.raises(ValueError, match="pauli"):
        _ = lestim.PauliString([4])
    with pytest.raises(ValueError):
        _ = lestim.PauliString([2**500])


def test_init_copy():
    p = lestim.PauliString("_XYZ")
    p2 = lestim.PauliString(p)
    assert p is not p2
    assert p == p2

    p = lestim.PauliString("-i_XYZ")
    p2 = lestim.PauliString(p)
    assert p is not p2
    assert p == p2


def test_commutes_different_lengths():
    x1000 = lestim.PauliString("X" * 1000)
    z1000 = lestim.PauliString("Z" * 1000)
    x1 = lestim.PauliString("X")
    z1 = lestim.PauliString("Z")
    assert x1.commutes(x1000)
    assert x1000.commutes(x1)
    assert z1.commutes(z1000)
    assert z1000.commutes(z1)
    assert not z1.commutes(x1000)
    assert not x1000.commutes(z1)
    assert not x1.commutes(z1000)
    assert not z1000.commutes(x1)


def test_pickle():
    import pickle

    t = lestim.PauliString.random(4)
    a = pickle.dumps(t)
    assert pickle.loads(a) == t

    t = lestim.PauliString("i_XYZ")
    a = pickle.dumps(t)
    assert pickle.loads(a) == t


def test_to_numpy():
    p = lestim.PauliString("_XYZ___XYXZYZ")

    xs, zs = p.to_numpy()
    assert xs.dtype == np.bool_
    assert zs.dtype == np.bool_
    np.testing.assert_array_equal(xs, [0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0])
    np.testing.assert_array_equal(zs, [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1])

    xs, zs = p.to_numpy(bit_packed=True)
    assert xs.dtype == np.uint8
    assert zs.dtype == np.uint8
    np.testing.assert_array_equal(xs, [0x86, 0x0B])
    np.testing.assert_array_equal(zs, [0x0C, 0x1D])


def test_from_numpy():
    p = lestim.PauliString.from_numpy(
        xs=np.array([0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0], dtype=np.bool_),
        zs=np.array([0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1], dtype=np.bool_))
    assert p == lestim.PauliString("_XYZ___XYXZYZ")

    p = lestim.PauliString.from_numpy(
        xs=np.array([0x86, 0x0B], dtype=np.uint8),
        zs=np.array([0x0C, 0x1D], dtype=np.uint8),
        num_qubits=13)

    assert p == lestim.PauliString("_XYZ___XYXZYZ")
    p = lestim.PauliString.from_numpy(
        xs=np.array([0x86, 0x0B], dtype=np.uint8),
        zs=np.array([0x0C, 0x1D], dtype=np.uint8),
        num_qubits=15,
        sign=1j)
    assert p == lestim.PauliString("i_XYZ___XYXZYZ__")


def test_from_numpy_bad_bit_packed_len():
    xs = np.array([0x86, 0x0B], dtype=np.uint8)
    zs = np.array([0x0C, 0x1D], dtype=np.uint8)
    with pytest.raises(ValueError, match="specify expected number"):
        lestim.PauliString.from_numpy(xs=xs, zs=zs)

    with pytest.raises(ValueError, match="between 9 and 16 bits"):
        lestim.PauliString.from_numpy(xs=xs, zs=zs, num_qubits=100)

    with pytest.raises(ValueError, match="between 9 and 16 bits"):
        lestim.PauliString.from_numpy(xs=xs, zs=zs, num_qubits=0)

    with pytest.raises(ValueError, match="between 9 and 16 bits"):
        lestim.PauliString.from_numpy(xs=xs, zs=zs, num_qubits=8)

    with pytest.raises(ValueError, match="between 9 and 16 bits"):
        lestim.PauliString.from_numpy(xs=xs, zs=zs, num_qubits=17)

    with pytest.raises(ValueError, match="between 0 and 0 bits"):
        lestim.PauliString.from_numpy(xs=xs[:0], zs=zs, num_qubits=9)

    with pytest.raises(ValueError, match="between 1 and 8 bits"):
        lestim.PauliString.from_numpy(xs=xs[:1], zs=zs, num_qubits=9)

    with pytest.raises(ValueError, match="between 1 and 8 bits"):
        lestim.PauliString.from_numpy(xs=xs, zs=zs[:1], num_qubits=9)

    with pytest.raises(ValueError, match="1-dimensional"):
        lestim.PauliString.from_numpy(xs=np.array([xs, xs]), zs=np.array([zs, zs]), num_qubits=9)

    with pytest.raises(ValueError, match="uint8"):
        lestim.PauliString.from_numpy(xs=np.array(xs, dtype=np.uint64), zs=np.array(xs, dtype=np.uint64), num_qubits=9)


def test_from_numpy_bad_bool_len():
    xs = np.array([0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0], dtype=np.bool_)
    zs = np.array([0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0], dtype=np.bool_)
    with pytest.raises(ValueError, match="shape=13"):
        lestim.PauliString.from_numpy(xs=xs, zs=zs, num_qubits=12)

    with pytest.raises(ValueError, match="shape=13"):
        lestim.PauliString.from_numpy(xs=xs, zs=zs, num_qubits=14)

    with pytest.raises(ValueError, match="shape=12"):
        lestim.PauliString.from_numpy(xs=xs[:-1], zs=zs, num_qubits=13)

    with pytest.raises(ValueError, match="shape=12"):
        lestim.PauliString.from_numpy(xs=xs, zs=zs[:-1], num_qubits=13)

    with pytest.raises(ValueError, match="Inconsistent"):
        lestim.PauliString.from_numpy(xs=xs, zs=zs[:-1])

    with pytest.raises(RuntimeError, match="Unable to cast"):
        lestim.PauliString.from_numpy(xs=xs, zs=zs, num_qubits=-1)


@pytest.mark.parametrize("n", [0, 1, 41, 42, 1023, 1024, 1025])
def test_to_from_numpy_round_trip(n: int):
    p = lestim.PauliString.random(n)
    xs, zs = p.to_numpy()
    p2 = lestim.PauliString.from_numpy(xs=xs, zs=zs, sign=p.sign)
    assert p2 == p
    xs, zs = p.to_numpy(bit_packed=True)
    p2 = lestim.PauliString.from_numpy(xs=xs, zs=zs, num_qubits=n, sign=p.sign)
    assert p2 == p


def test_to_unitary_matrix():
    np.testing.assert_array_equal(
        lestim.PauliString("").to_unitary_matrix(endian="little"),
        [[1]],
    )
    np.testing.assert_array_equal(
        lestim.PauliString("-").to_unitary_matrix(endian="big"),
        [[-1]],
    )
    np.testing.assert_array_equal(
        lestim.PauliString("i").to_unitary_matrix(endian="big"),
        [[1j]],
    )
    np.testing.assert_array_equal(
        lestim.PauliString("-i").to_unitary_matrix(endian="big"),
        [[-1j]],
    )

    np.testing.assert_array_equal(
        lestim.PauliString("I").to_unitary_matrix(endian="little"),
        [[1, 0], [0, 1]],
    )
    np.testing.assert_array_equal(
        lestim.PauliString("X").to_unitary_matrix(endian="little"),
        [[0, 1], [1, 0]],
    )
    np.testing.assert_array_equal(
        lestim.PauliString("Y").to_unitary_matrix(endian="little"),
        [[0, -1j], [1j, 0]],
    )
    np.testing.assert_array_equal(
        lestim.PauliString("iY").to_unitary_matrix(endian="little"),
        [[0, 1], [-1, 0]],
    )
    np.testing.assert_array_equal(
        lestim.PauliString("Z").to_unitary_matrix(endian="little"),
        [[1, 0], [0, -1]],
    )
    np.testing.assert_array_equal(
        lestim.PauliString("-Z").to_unitary_matrix(endian="little"),
        [[-1, 0], [0, 1]],
    )
    np.testing.assert_array_equal(
        lestim.PauliString("YY").to_unitary_matrix(endian="little"),
        [[0, 0, 0, -1], [0, 0, 1, 0], [0, 1, 0, 0], [-1, 0, 0, 0]],
    )
    np.testing.assert_array_equal(
        lestim.PauliString("-YZ").to_unitary_matrix(endian="little"),
        [[0, 1j, 0, 0], [-1j, 0, 0, 0], [0, 0, 0, -1j], [0, 0, 1j, 0]],
    )
    np.testing.assert_array_equal(
        lestim.PauliString("XYZ").to_unitary_matrix(endian="little"), [
            [0, 0, 0, -1j, 0, 0, 0, 0],
            [0, 0, -1j, 0, 0, 0, 0, 0],
            [0, 1j, 0, 0, 0, 0, 0, 0],
            [1j, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1j],
            [0, 0, 0, 0, 0, 0, 1j, 0],
            [0, 0, 0, 0, 0, -1j, 0, 0],
            [0, 0, 0, 0, -1j, 0, 0, 0],
        ])
    np.testing.assert_array_equal(
        lestim.PauliString("ZYX").to_unitary_matrix(endian="big"), [
            [0, 0, 0, -1j, 0, 0, 0, 0],
            [0, 0, -1j, 0, 0, 0, 0, 0],
            [0, 1j, 0, 0, 0, 0, 0, 0],
            [1j, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1j],
            [0, 0, 0, 0, 0, 0, 1j, 0],
            [0, 0, 0, 0, 0, -1j, 0, 0],
            [0, 0, 0, 0, -1j, 0, 0, 0],
        ])


def test_from_unitary_matrix():
    assert lestim.PauliString.from_unitary_matrix(
        [[1]]
    ) == lestim.PauliString("")
    assert lestim.PauliString.from_unitary_matrix(
        [[-1]]
    ) == lestim.PauliString("-")
    assert lestim.PauliString.from_unitary_matrix(
        [[1j]]
    ) == lestim.PauliString("i")
    assert lestim.PauliString.from_unitary_matrix(
        [[-1j]]
    ) == lestim.PauliString("-i")

    assert lestim.PauliString.from_unitary_matrix(
        [[1, 0], [0, 1]]
    ) == lestim.PauliString("I")
    assert lestim.PauliString.from_unitary_matrix(
        [[0, 1], [1, 0]]
    ) == lestim.PauliString("X")
    assert lestim.PauliString.from_unitary_matrix(
        [[0, -1j], [1j, 0]]
    ) == lestim.PauliString("Y")
    assert lestim.PauliString.from_unitary_matrix(
        [[1, 0], [0, -1]]
    ) == lestim.PauliString("Z")

    assert lestim.PauliString.from_unitary_matrix(
        [[0, 1], [-1, 0]]
    ) == lestim.PauliString("iY")
    assert lestim.PauliString.from_unitary_matrix(
        [[0, 1j], [-1j, 0]]
    ) == lestim.PauliString("-Y")
    assert lestim.PauliString.from_unitary_matrix(
        [[1j, 0], [0, -1j]]
    ) == lestim.PauliString("iZ")
    assert lestim.PauliString.from_unitary_matrix(
        [[-1, 0], [0, 1]]
    ) == lestim.PauliString("-Z")

    assert lestim.PauliString.from_unitary_matrix(
        [[1]], unsigned=True
    ) == lestim.PauliString("")
    assert lestim.PauliString.from_unitary_matrix(
        [[-1]], unsigned=True
    ) == lestim.PauliString("")
    assert lestim.PauliString.from_unitary_matrix(
        [[0, 1], [-1, 0]], unsigned=True
    ) == lestim.PauliString("Y")
    assert lestim.PauliString.from_unitary_matrix(
        [[0, +1 * 1j**0.1], [-1 * 1j**0.1, 0]], unsigned=True
    ) == lestim.PauliString("Y")

    assert lestim.PauliString.from_unitary_matrix([
        [0, 0, 0, -1j, 0, 0, 0, 0],
        [0, 0, -1j, 0, 0, 0, 0, 0],
        [0, 1j, 0, 0, 0, 0, 0, 0],
        [1j, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1j],
        [0, 0, 0, 0, 0, 0, 1j, 0],
        [0, 0, 0, 0, 0, -1j, 0, 0],
        [0, 0, 0, 0, -1j, 0, 0, 0],
    ], endian="little") == lestim.PauliString("XYZ")
    assert lestim.PauliString.from_unitary_matrix([
        [0, 0, 0, -1j, 0, 0, 0, 0],
        [0, 0, -1j, 0, 0, 0, 0, 0],
        [0, 1j, 0, 0, 0, 0, 0, 0],
        [1j, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1j],
        [0, 0, 0, 0, 0, 0, 1j, 0],
        [0, 0, 0, 0, 0, -1j, 0, 0],
        [0, 0, 0, 0, -1j, 0, 0, 0],
    ], endian="big") == lestim.PauliString("ZYX")
    assert lestim.PauliString.from_unitary_matrix(np.array([
        [0, 0, 0, -1j, 0, 0, 0, 0],
        [0, 0, -1j, 0, 0, 0, 0, 0],
        [0, 1j, 0, 0, 0, 0, 0, 0],
        [1j, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1j],
        [0, 0, 0, 0, 0, 0, 1j, 0],
        [0, 0, 0, 0, 0, -1j, 0, 0],
        [0, 0, 0, 0, -1j, 0, 0, 0],
    ]) * 1j**0.1, endian="big", unsigned=True) == lestim.PauliString("ZYX")
    assert lestim.PauliString.from_unitary_matrix(np.array([
        [0, 0, 0, -1j, 0, 0, 0, 0],
        [0, 0, -1j, 0, 0, 0, 0, 0],
        [0, 1j, 0, 0, 0, 0, 0, 0],
        [1j, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1j],
        [0, 0, 0, 0, 0, 0, 1j, 0],
        [0, 0, 0, 0, 0, -1j, 0, 0],
        [0, 0, 0, 0, -1j, 0, 0, 0],
    ]) * -1, endian="big", unsigned=True) == lestim.PauliString("ZYX")


def test_from_unitary_matrix_detect_bad_matrix():
    with pytest.raises(ValueError, match="power of 2"):
        lestim.PauliString.from_unitary_matrix([])
    with pytest.raises(ValueError, match="row with no non-zero"):
        lestim.PauliString.from_unitary_matrix([[]])
    with pytest.raises(ValueError, match="row with no non-zero"):
        lestim.PauliString.from_unitary_matrix([[0]])
    with pytest.raises(ValueError, match="values besides 0, 1,"):
        lestim.PauliString.from_unitary_matrix([[0.5]])
    with pytest.raises(ValueError, match="isn't square"):
        lestim.PauliString.from_unitary_matrix([[1, 0]])
    with pytest.raises(ValueError, match="no non-zero entries"):
        lestim.PauliString.from_unitary_matrix([[1], [0]])
    with pytest.raises(ValueError, match="different lengths"):
        lestim.PauliString.from_unitary_matrix([[0, 1], [1]])
    with pytest.raises(ValueError, match="two non-zero entries"):
        lestim.PauliString.from_unitary_matrix([[1, 1],
                                              [0, 1]])
    with pytest.raises(ValueError, match="which qubits are flipped"):
        lestim.PauliString.from_unitary_matrix([[1, 0],
                                              [1, 0]])
    with pytest.raises(ValueError, match="isn't square"):
        lestim.PauliString.from_unitary_matrix([[1, 0, 0],
                                              [0, 1, 0]])
    with pytest.raises(ValueError, match="consistent phase flips"):
        lestim.PauliString.from_unitary_matrix([[1, 0],
                                              [0, 1j]])

    with pytest.raises(ValueError, match="power of 2"):
        lestim.PauliString.from_unitary_matrix([[1, 0, 0],
                                              [0, 1, 0],
                                              [0, 0, 1]])
    with pytest.raises(ValueError, match="which qubits are flipped"):
        lestim.PauliString.from_unitary_matrix([[1, 0, 0, 0],
                                              [0, 1, 0, 0],
                                              [0, 0, 0, 1],
                                              [0, 0, 1, 0]])
    with pytest.raises(ValueError, match="consistent phase flips"):
        lestim.PauliString.from_unitary_matrix([[1, 0, 0, 0],
                                              [0, 1, 0, 0],
                                              [0, 0, 1, 0],
                                              [0, 0, 0, -1]])
    with pytest.raises(ValueError, match="consistent phase flips"):
        lestim.PauliString.from_unitary_matrix([[1, 0, 0, 0],
                                              [0, 1, 0, 0],
                                              [0, 0, -1, 0],
                                              [0, 0, 0, 1]])


@pytest.mark.parametrize("n,endian", itertools.product(range(8), ['little', 'big']))
def test_fuzz_to_from_unitary_matrix(n: int, endian: str):
    p = lestim.PauliString.random(n, allow_imaginary=True)
    u = p.to_unitary_matrix(endian=endian)
    r = lestim.PauliString.from_unitary_matrix(u, endian=endian)
    assert p == r

    via_tableau = lestim.Tableau.from_unitary_matrix(u, endian=endian).to_pauli_string()
    r.sign = +1
    assert via_tableau == r


def test_before_after():
    before = lestim.PauliString("XXXYYYZZZ")
    after = lestim.PauliString("XYXYZYXZZ")
    assert before.after(lestim.Circuit("C_XYZ 1 4 6")) == after
    assert before.after(lestim.Circuit("C_XYZ 1 4 6")[0]) == after
    assert before.after(lestim.Tableau.from_named_gate("C_XYZ"), targets=[1, 4, 6]) == after
    assert after.before(lestim.Circuit("C_XYZ 1 4 6")) == before
    assert after.before(lestim.Circuit("C_XYZ 1 4 6")[0]) == before
    assert after.before(lestim.Tableau.from_named_gate("C_XYZ"), targets=[1, 4, 6]) == before


def test_iter_small():
    assert list(lestim.PauliString.iter_all(0)) == [lestim.PauliString(0)]
    assert list(lestim.PauliString.iter_all(1)) == [
        lestim.PauliString("_"),
        lestim.PauliString("X"),
        lestim.PauliString("Y"),
        lestim.PauliString("Z"),
    ]
    assert list(lestim.PauliString.iter_all(1, max_weight=-1)) == [
    ]
    assert list(lestim.PauliString.iter_all(1, max_weight=0)) == [
        lestim.PauliString("_"),
    ]
    assert list(lestim.PauliString.iter_all(1, max_weight=1)) == [
        lestim.PauliString("_"),
        lestim.PauliString("X"),
        lestim.PauliString("Y"),
        lestim.PauliString("Z"),
    ]
    assert list(lestim.PauliString.iter_all(1, min_weight=1, max_weight=1)) == [
        lestim.PauliString("X"),
        lestim.PauliString("Y"),
        lestim.PauliString("Z"),
    ]
    assert list(lestim.PauliString.iter_all(2, min_weight=1, max_weight=1, allowed_paulis="XY")) == [
        lestim.PauliString("X_"),
        lestim.PauliString("Y_"),
        lestim.PauliString("_X"),
        lestim.PauliString("_Y"),
    ]

    with pytest.raises(ValueError, match="characters other than"):
        lestim.PauliString.iter_all(2, allowed_paulis="A")


def test_iter_reusable():
    v = lestim.PauliString.iter_all(2)
    vs1 = list(v)
    vs2 = list(v)
    assert vs1 == vs2
    assert len(vs1) == 4**2


def test_backwards_compatibility_init():
    assert lestim.PauliString() == lestim.PauliString("+")
    assert lestim.PauliString(5) == lestim.PauliString("+_____")
    assert lestim.PauliString([1, 2, 3]) == lestim.PauliString("+XYZ")
    assert lestim.PauliString("XYZ") == lestim.PauliString("+XYZ")
    assert lestim.PauliString(lestim.PauliString("XYZ")) == lestim.PauliString("+XYZ")
    assert lestim.PauliString("X" for _ in range(4)) == lestim.PauliString("+XXXX")

    # These keywords have been removed from the documentation and the .pyi, but
    # their functionality needs to be maintained for backwards compatibility.
    # noinspection PyArgumentList
    assert lestim.PauliString(num_qubits=5) == lestim.PauliString("+_____")
    # noinspection PyArgumentList
    assert lestim.PauliString(pauli_indices=[1, 2, 3]) == lestim.PauliString("+XYZ")
    # noinspection PyArgumentList
    assert lestim.PauliString(text="XYZ") == lestim.PauliString("+XYZ")
    # noinspection PyArgumentList
    assert lestim.PauliString(other=lestim.PauliString("XYZ")) == lestim.PauliString("+XYZ")


def test_pauli_indices():
    assert lestim.PauliString().pauli_indices() == []
    assert lestim.PauliString().pauli_indices("X") == []
    assert lestim.PauliString().pauli_indices("I") == []
    assert lestim.PauliString(5).pauli_indices() == []
    assert lestim.PauliString(5).pauli_indices("X") == []
    assert lestim.PauliString(5).pauli_indices("I") == [0, 1, 2, 3, 4]
    assert lestim.PauliString("X1000").pauli_indices() == [1000]
    assert lestim.PauliString("Y1000").pauli_indices() == [1000]
    assert lestim.PauliString("Z1000").pauli_indices() == [1000]
    assert lestim.PauliString("X1000").pauli_indices("YZ") == []
    assert lestim.PauliString("Y1000").pauli_indices("XZ") == []
    assert lestim.PauliString("Z1000").pauli_indices("XY") == []
    assert lestim.PauliString("X1000").pauli_indices("X") == [1000]
    assert lestim.PauliString("Y1000").pauli_indices("Y") == [1000]
    assert lestim.PauliString("Z1000").pauli_indices("Z") == [1000]

    assert lestim.PauliString("_XYZ").pauli_indices("x") == [1]
    assert lestim.PauliString("_XYZ").pauli_indices("X") == [1]
    assert lestim.PauliString("_XYZ").pauli_indices("y") == [2]
    assert lestim.PauliString("_XYZ").pauli_indices("Y") == [2]
    assert lestim.PauliString("_XYZ").pauli_indices("z") == [3]
    assert lestim.PauliString("_XYZ").pauli_indices("Z") == [3]
    assert lestim.PauliString("_XYZ").pauli_indices("I") == [0]
    assert lestim.PauliString("_XYZ").pauli_indices("_") == [0]
    with pytest.raises(ValueError, match="Invalid character"):
<<<<<<< HEAD
        assert lestim.PauliString("_XYZ").pauli_indices("k")


def test_before_reset():
    assert lestim.PauliString("Z").before(lestim.Circuit("R 0")) == lestim.PauliString("_")
    assert lestim.PauliString("Z").before(lestim.Circuit("MR 0")) == lestim.PauliString("_")
    assert lestim.PauliString("Z").before(lestim.Circuit("M 0")) == lestim.PauliString("Z")

    assert lestim.PauliString("X").before(lestim.Circuit("RX 0")) == lestim.PauliString("_")
    assert lestim.PauliString("X").before(lestim.Circuit("MRX 0")) == lestim.PauliString("_")
    assert lestim.PauliString("X").before(lestim.Circuit("MX 0")) == lestim.PauliString("X")

    assert lestim.PauliString("Y").before(lestim.Circuit("RY 0")) == lestim.PauliString("_")
    assert lestim.PauliString("Y").before(lestim.Circuit("MRY 0")) == lestim.PauliString("_")
    assert lestim.PauliString("Y").before(lestim.Circuit("MY 0")) == lestim.PauliString("Y")

    with pytest.raises(ValueError):
        lestim.PauliString("Z").before(lestim.Circuit("RX 0"))
    with pytest.raises(ValueError):
        lestim.PauliString("Z").before(lestim.Circuit("RY 0"))
    with pytest.raises(ValueError):
        lestim.PauliString("Z").before(lestim.Circuit("MRX 0"))
    with pytest.raises(ValueError):
        lestim.PauliString("Z").before(lestim.Circuit("MRY 0"))
    with pytest.raises(ValueError):
        lestim.PauliString("Z").before(lestim.Circuit("MX 0"))
    with pytest.raises(ValueError):
        lestim.PauliString("Z").before(lestim.Circuit("MY 0"))

def test_constructor_from_dict():
    # Values are single Pauli -> Key is the qubit index:
    assert lestim.PauliString({2: "X", 4: "Z"}) == lestim.PauliString("__X_Z")
    assert lestim.PauliString({0: 1, 1: 2}) == lestim.PauliString("XY")
    assert lestim.PauliString({1: 1, 3: 2, 5: "Z"}) == lestim.PauliString("_X_Y_Z")
    assert lestim.PauliString({1: 0, 3: "I", 4: "_"}) == lestim.PauliString("_____")
    assert lestim.PauliString({0: "X", 2: "x", 4: "y"}) == lestim.PauliString("X_X_Y") # Case-insensitive
    assert lestim.PauliString({}) == lestim.PauliString("")

    # Values are iterable -> Key is the Pauli:
    assert lestim.PauliString({"X": [0], "Z": [1]}) == lestim.PauliString("XZ")
    assert lestim.PauliString({1: [0], 3: [1]}) == lestim.PauliString("XZ")
    assert lestim.PauliString({"X": [2], "Z": [4], "Y": [6], "I": [5]}) == lestim.PauliString("__X_Z_Y")
    assert lestim.PauliString({"X": [0], "Z": [1,2]}) == lestim.PauliString("XZZ")
    assert lestim.PauliString({"x": [0,2], "Y": [4]}) == lestim.PauliString("X_X_Y") # Case-insensitive
    assert lestim.PauliString({"I": [1,2]}) == lestim.PauliString("___")
    assert lestim.PauliString({"I": []}) == lestim.PauliString("")
    assert lestim.PauliString({"I": [9]}) == lestim.PauliString(10)
    assert lestim.PauliString({0: [9]}) == lestim.PauliString(10)
    assert lestim.PauliString({"_": [9]}) == lestim.PauliString(10)

    # Acceptable collisions:
    assert lestim.PauliString({"X": [2], "I": [2]}) == lestim.PauliString("__X") # Trivial Pauli should not cause a conflict
    assert lestim.PauliString({"X": [2], 1: [2]}) == lestim.PauliString("__X") # Same Pauli should not cause conflict between int/str
    assert lestim.PauliString({"X": [2], "I": [0,1,2,3], "Z": [0], 0: [0,1,2,3], "Y": [1], "_": [0,1,2,3]}) == lestim.PauliString("ZYX_") # A more complex example

def test_constructor_from_dict_errors():
    with pytest.raises(ValueError, match="keys must all be ints"):
        lestim.PauliString({"X": 0}) # When value is non-itetable, key must be int (index)

    with pytest.raises(ValueError, match="Don't know how to convert"):
        lestim.PauliString({"A": [0]})

    with pytest.raises(ValueError, match="Don't know how to convert"):
        lestim.PauliString({0: "A"})

    with pytest.raises(ValueError, match="Don't know how to convert"):
        lestim.PauliString({0: 4}) # Paulis correspond to 0-3

    with pytest.raises(ValueError, match="Don't know how to convert"):
        lestim.PauliString({0: -1}) # Paulis correspond to 0-3

    with pytest.raises(ValueError, match="Don't know how to convert"):
        lestim.PauliString({"ZX": [0]}) # Paulis need to be single characters

    with pytest.raises(ValueError, match="Pauli keys with iterable values"):
        lestim.PauliString({"X": "not an iterable"})

    with pytest.raises(ValueError, match="Qubit index must be an int"):
        lestim.PauliString({"Y": [0, "not an int"]})

    with pytest.raises(ValueError, match="keys must all be ints"):
        lestim.PauliString({"X": 0, 1: "Y"})

    with pytest.raises(ValueError, match="Qubit index must be an int"):
        lestim.PauliString({"X": [0], 1: "Y"})

    with pytest.raises(ValueError, match="Qubit index must be an int"):
        lestim.PauliString({"X": [0], 1: ["Y"]})

    with pytest.raises(ValueError, match="same qubit index"):
        lestim.PauliString({"X": [0], "Y": [0]}) # Different non-trivial Paulies can't use the same index

    with pytest.raises(ValueError, match="same qubit index"):
        lestim.PauliString({"Z": [1], "Y": [4,1]}) # Different non-trivial Paulies can't use the same index

    with pytest.raises(ValueError, match="same qubit index"):
        lestim.PauliString({"I": [0,1,4], "Z": [1], "Y": [4,1]}) # Different non-trivial Paulies can't use the same index

    with pytest.raises(ValueError, match="keys must all be ints"):
        lestim.PauliString({(): []})

    with pytest.raises(ValueError, match="keys must all be ints"):
        lestim.PauliString({(): 0})

    with pytest.raises(ValueError, match="Qubit index must be an int"):
        lestim.PauliString({"X": [()]})

    with pytest.raises(ValueError, match="Qubit index must be non-negative"):
        lestim.PauliString({"X": [-1]})

    with pytest.raises(ValueError, match="Qubit index must be non-negative"):
        lestim.PauliString({-1: "X"})
    
    with pytest.raises(ValueError, match="Qubit index must be non-negative"):
        lestim.PauliString({"I": [-1]})
=======
        assert stim.PauliString("_XYZ").pauli_indices("k")


def test_before_reset():
    assert stim.PauliString("Z").before(stim.Circuit("R 0")) == stim.PauliString("_")
    assert stim.PauliString("Z").before(stim.Circuit("MR 0")) == stim.PauliString("_")
    assert stim.PauliString("Z").before(stim.Circuit("M 0")) == stim.PauliString("Z")

    assert stim.PauliString("X").before(stim.Circuit("RX 0")) == stim.PauliString("_")
    assert stim.PauliString("X").before(stim.Circuit("MRX 0")) == stim.PauliString("_")
    assert stim.PauliString("X").before(stim.Circuit("MX 0")) == stim.PauliString("X")

    assert stim.PauliString("Y").before(stim.Circuit("RY 0")) == stim.PauliString("_")
    assert stim.PauliString("Y").before(stim.Circuit("MRY 0")) == stim.PauliString("_")
    assert stim.PauliString("Y").before(stim.Circuit("MY 0")) == stim.PauliString("Y")

    with pytest.raises(ValueError):
        stim.PauliString("Z").before(stim.Circuit("RX 0"))
    with pytest.raises(ValueError):
        stim.PauliString("Z").before(stim.Circuit("RY 0"))
    with pytest.raises(ValueError):
        stim.PauliString("Z").before(stim.Circuit("MRX 0"))
    with pytest.raises(ValueError):
        stim.PauliString("Z").before(stim.Circuit("MRY 0"))
    with pytest.raises(ValueError):
        stim.PauliString("Z").before(stim.Circuit("MX 0"))
    with pytest.raises(ValueError):
        stim.PauliString("Z").before(stim.Circuit("MY 0"))

def test_constructor_from_dict():
    # Values are single Pauli -> Key is the qubit index:
    assert stim.PauliString({2: "X", 4: "Z"}) == stim.PauliString("__X_Z")
    assert stim.PauliString({0: 1, 1: 2}) == stim.PauliString("XY")
    assert stim.PauliString({1: 1, 3: 2, 5: "Z"}) == stim.PauliString("_X_Y_Z")
    assert stim.PauliString({1: 0, 3: "I", 4: "_"}) == stim.PauliString("_____")
    assert stim.PauliString({0: "X", 2: "x", 4: "y"}) == stim.PauliString("X_X_Y") # Case-insensitive
    assert stim.PauliString({}) == stim.PauliString("")

    # Values are iterable -> Key is the Pauli:
    assert stim.PauliString({"X": [0], "Z": [1]}) == stim.PauliString("XZ")
    assert stim.PauliString({1: [0], 3: [1]}) == stim.PauliString("XZ")
    assert stim.PauliString({"X": [2], "Z": [4], "Y": [6], "I": [5]}) == stim.PauliString("__X_Z_Y")
    assert stim.PauliString({"X": [0], "Z": [1,2]}) == stim.PauliString("XZZ")
    assert stim.PauliString({"x": [0,2], "Y": [4]}) == stim.PauliString("X_X_Y") # Case-insensitive
    assert stim.PauliString({"I": [1,2]}) == stim.PauliString("___")
    assert stim.PauliString({"I": []}) == stim.PauliString("")
    assert stim.PauliString({"I": [9]}) == stim.PauliString(10)
    assert stim.PauliString({0: [9]}) == stim.PauliString(10)
    assert stim.PauliString({"_": [9]}) == stim.PauliString(10)

    # Acceptable collisions:
    assert stim.PauliString({"X": [2], "I": [2]}) == stim.PauliString("__X") # Trivial Pauli should not cause a conflict
    assert stim.PauliString({"X": [2], 1: [2]}) == stim.PauliString("__X") # Same Pauli should not cause conflict between int/str
    assert stim.PauliString({"X": [2], "I": [0,1,2,3], "Z": [0], 0: [0,1,2,3], "Y": [1], "_": [0,1,2,3]}) == stim.PauliString("ZYX_") # A more complex example

def test_constructor_from_dict_errors():
    with pytest.raises(ValueError, match="keys must all be ints"):
        stim.PauliString({"X": 0}) # When value is non-itetable, key must be int (index)

    with pytest.raises(ValueError, match="Don't know how to convert"):
        stim.PauliString({"A": [0]})

    with pytest.raises(ValueError, match="Don't know how to convert"):
        stim.PauliString({0: "A"})

    with pytest.raises(ValueError, match="Don't know how to convert"):
        stim.PauliString({0: 4}) # Paulis correspond to 0-3

    with pytest.raises(ValueError, match="Don't know how to convert"):
        stim.PauliString({0: -1}) # Paulis correspond to 0-3

    with pytest.raises(ValueError, match="Don't know how to convert"):
        stim.PauliString({"ZX": [0]}) # Paulis need to be single characters

    with pytest.raises(ValueError, match="Pauli keys with iterable values"):
        stim.PauliString({"X": "not an iterable"})

    with pytest.raises(ValueError, match="Qubit index must be an int"):
        stim.PauliString({"Y": [0, "not an int"]})

    with pytest.raises(ValueError, match="keys must all be ints"):
        stim.PauliString({"X": 0, 1: "Y"})

    with pytest.raises(ValueError, match="Qubit index must be an int"):
        stim.PauliString({"X": [0], 1: "Y"})

    with pytest.raises(ValueError, match="Qubit index must be an int"):
        stim.PauliString({"X": [0], 1: ["Y"]})

    with pytest.raises(ValueError, match="same qubit index"):
        stim.PauliString({"X": [0], "Y": [0]}) # Different non-trivial Paulies can't use the same index

    with pytest.raises(ValueError, match="same qubit index"):
        stim.PauliString({"Z": [1], "Y": [4,1]}) # Different non-trivial Paulies can't use the same index

    with pytest.raises(ValueError, match="same qubit index"):
        stim.PauliString({"I": [0,1,4], "Z": [1], "Y": [4,1]}) # Different non-trivial Paulies can't use the same index

    with pytest.raises(ValueError, match="keys must all be ints"):
        stim.PauliString({(): []})

    with pytest.raises(ValueError, match="keys must all be ints"):
        stim.PauliString({(): 0})

    with pytest.raises(ValueError, match="Qubit index must be an int"):
        stim.PauliString({"X": [()]})

    with pytest.raises(ValueError, match="Qubit index must be non-negative"):
        stim.PauliString({"X": [-1]})

    with pytest.raises(ValueError, match="Qubit index must be non-negative"):
        stim.PauliString({-1: "X"})
    
    with pytest.raises(ValueError, match="Qubit index must be non-negative"):
        stim.PauliString({"I": [-1]})
>>>>>>> 1a67d3a9 (feat: Sync with Stim (#32))
