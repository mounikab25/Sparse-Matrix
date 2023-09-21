import pytest
from sparse_recommender import SparMtx

#checking if the values are stored in the dictionary
def test_create_mov():
    mtx = SparMtx()
    mtx.set(1,1,3)
    mtx.set(2,3,7)
    assert mtx.len() != 0

#setting the value
def test_set_mov():
    mtx = SparMtx()
    mtx.set(2,0,8)
    assert mtx.len() == 1

#getting the value
def test_get_mov():
    mtx = SparMtx()
    mtx.set(1,0,3)
    assert mtx.get(1,0) == 3

#recommend that is multiply and get the resulting vector
def test_recommend_mov():
    mtx = SparMtx()
    mtx.set(0,1,4)
    mtx.set(1,2,2)
    vect = [2,3,2]
    assert mtx.recommend(vect) == [12,4,0]

#add two matrices
def test_add_mov():
    mtx1 = SparMtx()
    mtx1.set(1,0,4)
    mtx1.set(2,3,3)
    mtx2 = SparMtx()
    mtx2.set(1,0,2)
    mtx2.set(2,3,1)
    mtx1.add_movie(mtx2)
    assert mtx1.get(1,0) == 6

#trying to set zero value
def test_zero():
    mtx = SparMtx()
    mtx.set(2,3,0)
    assert mtx.len() == 0

#sparse to dense matrix
def test_den():
    mtx = SparMtx()
    mtx.set(1,2,3)
    mtx.set(0,3,6)
    mtx.set(2,1,5)
    assert mtx.to_dense() == [[0,0,0,6], [0,0,3,0], [0,5,0,0]]

#checking for negative row index
def test_neg_rowindex():
    with pytest.raises(ValueError):
        mtx = SparMtx()
        mtx.set(-1,2,7)
    assert mtx.len() == 0

#checking for negative column index
def test_neg_colindex():
    with pytest.raises(ValueError):
        mtx = SparMtx()
        mtx.set(2,-1,9)
    assert mtx.len() == 0

#if the row and column dimensions of the matrices doesn't match
def test_inval_recommend_vect():
    mtx = SparMtx()
    mtx.set(0,1,1)
    mtx.set(1,0,3)
    vect = [5]
    with pytest.raises(ValueError):
        mtx.recommend(vect)

#adding a non matrix to a matrix
def test_inval_add():
    mtx1 = SparMtx()
    mtx2 = "Addition of string to amtrix is not possible"
    with pytest.raises(AttributeError):
        mtx1.add_movie(mtx2)
    