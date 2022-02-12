# import os, sys
# sys.path.append('../')

from timeDP2.utils import *
from timeDP2.mechanism import bounded_laplace_mechanism as BLM
from timeDP2.mechanism import laplace_mechanism as LM

class TimeDP:
    
    def __init__(self, epsilon, delta, mechanism_type : str):
        '''
        This class is a noise giving class. It takes the gradient and calculates new synthezied series data
        you can choose two types of mechanism. Original laplace mechanism or Bounded Laplace Mechanism
        mechanism_type : 1) laplace, 2) bouned_laplace
        '''
        self.epsilon = epsilon
        self.delta = delta 
        self.mechanism_type = mechanism_type
        self.mechanism = self._dp_mechanism()
    
    def _dp_mechanism(self):
        if self.mechanism_type == 'laplace':
            return LM.laplace_mechanism
        else :
            return BLM.boundedlaplacemechanism
        
    def calculate_dp_value(self, val, sens):
        '''
        requires value(val) and sensitivity(sens)
        '''
        if self.mechanism_type == 'laplace':
            return self.mechanism(value=val, sensitivity=sens, epsilon=self.epsilon)
        else :
            return self.mechanism(value=val, D=None, b=0.1, epsilon=self.epsilon, delta = self.delta)


class Vector_creator:
    
    def __init__(self, vector: np.array, timedp: object):
        self.vector = vector
        self.vector_length = len(vector)
        self.timedp = timedp
        self.extended_vector = self.make_extended_vector()
        self.coordinates = self.make_coordinates()
        self.gradient_list = self.prepare_for_gradient()
    
    def make_extended_vector(self):
        '''
        makes extended vector
        '''
        return make_extended_vector(vector=self.vector)
    
    def make_coordinates(self):
        '''
        makes x and y coordinate list 
        '''
        extend_vector_length = self.vector_length * 2
        xs = [x for x in x in range(0, extend_vector_length)]
        return make_coordinate_list(xs, self.extended_vector, 2)
    
    def prepare_for_gradient(self):
        return give_calculated_gradient_list(self.extended_vector, step=2)
    
    def make_new_gradient(self):
        pass
    
    def make_new_value_based_on_new_gradient:
        pass
        
        
        
