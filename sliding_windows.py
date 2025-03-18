# coding = utf-8
# author = cch
# date = 20250318
# description: introduction for function numpy.lib.stride_tricks.as_strided

import numpy as np
from typing import Tuple


class Slide_wins:
    """
    Performing a 2D sliding window operation on a 2D array.
    Methods: 
    slide_wins: Performing a 2D sliding window operation on a 2D array.
    run: run.
    """ 
    def __init__(self,data: np.ndarray, win_size: Tuple, win_step: Tuple) -> None:
        """
        initialize class
        param data: np.ndarray.
        param win_size: tuple.
        param win_step: tuple.
        return a 4D array whose shape is data_shape + win_size
        """
        print("data have to be c_contiguous")
        self.data = data
        self.win_size = win_size
        self.win_step = win_step
        return None

    def slide_wins(self,data: np.ndarray, win_size: Tuple, win_step: Tuple) -> np.ndarray:
        """
        Performing a 2D sliding window operation on a 2D array.
        param data: np.ndarray.
        param win_size: tuple.
        param win_step: tuple.
        return a 4D array whose shape is data_shape + win_size
        """
        num_row = (data.shape[0] - win_size[0]) // win_step[0] + 1
        num_col = (data.shape[1] - win_size[1]) // win_step[1] + 1
        shape = (num_row, num_col) + win_size
        strides = data.itemsize * np.array([win_step[0] * Col, win_step[1] * 1, 1 * Col, 1 * 1])
        results = np.lib.stride_tricks.as_strided(data, shape=shape, strides=strides,writeable=False)
        return results
    def run(self):
        if self.data.flags.c_contiguous:
            print("data is c_contiguous")
            return self.slide_wins(data=self.data,win_size=self.win_size,win_step=self.win_step)
        else:
            print("data is not c_contiguous. please choose: \n n (terminate) or y (transform data)")
            s = input("please input your choice: ")
            if s == "n":
                raise ValueError("data is not c_contiguous")
            if s == "y":
                self.new_data = np.ascontiguousarray(self.data)
                return self.slide_wins(data=self.new_data,win_size=self.win_size,win_step=self.win_step)
            
                
if __name__ == "__main__":
    Row, Col = 11, 9
    x = np.arange(Row * Col).reshape(Row,Col)
    print(x)

    # sliding wins
    win_size = (5,3)
    win_step = (3,2)

    sw = Slide_wins(x,win_size,win_step)
    print(sw.run())

