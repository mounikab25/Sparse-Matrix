class SparMtx:
    def __init__(self):
        self.dict = {}

    #setting a value
    def set(self,row,col,val):
        if row<0 or col<0:
            raise ValueError("Row and column dimensions should be positive")
        if val!=0:
            if row not in self.dict:
                self.dict[row] = {}
            self.dict[row][col] = val
    
    #finding the length of the dictionary
    def len(self):
        tot_len = 0
        for row in self.dict.values():
            tot_len += len(row)
        return tot_len
    
    #fetching the value
    def get(self,row,col):
        itm = self.dict.get(row,{})
        return itm.get(col,0)
    
    #multiplying the matrix and the vector and the returning the result matrix
    def recommend(self,vect):
        values = self.dict.values()
        max_idx_per_item = []
        for row_data in values:
            max_col_for_row = max(row_data.keys(),default = 0)
            max_idx_per_item.append(max_col_for_row)
        max_idx = max(max_idx_per_item,default=0)
        if len(vect)<=max_idx:
            raise ValueError("The matrix size id not compatible for multiplication")
        res = [0]*len(vect)
        for row in self.dict:
            for col in self.dict[row]:
                res[row] += self.dict[row][col]*vect[col]
        return res    
        
    #adding two matrices
    def add_movie(self,mtx):
        for row in mtx.dict:
            for col in mtx.dict[row]:
                self.set(row,col,self.get(row,col)+mtx.get(row,col))
        return self
    
    #converting sparse matrix to dense matrix
    def to_dense(self):
        max_row = max(self.dict.keys())+1
        max_row_per_item = []
        for cols in self.dict.values():
            max_col_per_item = max(cols.keys()) if cols else 0
            max_row_per_item.append(max_col_per_item)
        max_col = max(max_row_per_item,default=0)+1
        den_mtx = []
        for _ in range(max_row):
            row = [0]*max_col
            den_mtx.append(row)
        for row in self.dict:
            for col in self.dict[row]:
                den_mtx[row][col] = self.dict[row][col]
        return den_mtx