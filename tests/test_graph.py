import src.graph as graph
import unittest
import math


SIN_PI_FOURTH = 0.5*math.sqrt(2.0)
class Test_Creating_Graph_With_Unit_Values_At_Data_Points(unittest.TestCase):

	def test_00_10_11_01_square(self):
		points = [(0,0,1),(1,0,1),(1,1,1),(0,1,1)]
		expected_graph_points = [
			(-SIN_PI_FOURTH, -SIN_PI_FOURTH), 
			(1+SIN_PI_FOURTH, -SIN_PI_FOURTH), 
			(1+SIN_PI_FOURTH, 1+SIN_PI_FOURTH), 
			(-SIN_PI_FOURTH, 1+SIN_PI_FOURTH), 
		]
		graph_points = graph._get_points(points)
		for i in range(4):
			self.assertAlmostEqual(graph_points[i][0],expected_graph_points[i][0],delta=1e-10)
			self.assertAlmostEqual(graph_points[i][1],expected_graph_points[i][1],delta=1e-10)
		
		# reversed order of data points yields identical set of graph points, 
		# only in reversed order
		points.reverse()
		expected_graph_points.reverse()
		graph_points = graph._get_points(points)
		for i in range(4):
			self.assertAlmostEqual(graph_points[i][0],expected_graph_points[i][0],delta=1e-10)
			self.assertAlmostEqual(graph_points[i][1],expected_graph_points[i][1],delta=1e-10)


class Test_Single_Normal(unittest.TestCase):
    
	def test_unit_vectors_in_positive_x_direction(self):
		vectors = [(1,0),(1,0)]
		expected_normal = [0,-1]
		self.assertEqual(graph._get_normal(*vectors),expected_normal)

	def test_unit_vectors_in_negative_x_direction(self):
		vectors = [(-1,0),(-1,0)]
		expected_normal = [0,1]
		self.assertEqual(graph._get_normal(*vectors),expected_normal)

	def test_first_vector_in_positive_second_in_negative_x_direction(self):
		vectors = [(1,0),(-1,0)]
		expected_normal = [1,0]
		self.assertEqual(graph._get_normal(*vectors),expected_normal)

	def test_first_vector_in_negative_second_in_positive_x_direction(self):
		vectors = [(-1,0),(1,0)]
		expected_normal = [-1,0]
		self.assertEqual(graph._get_normal(*vectors),expected_normal)

	def test_unit_vectors_in_positive_y_direction(self):
		vectors = [(0,1),(0,1)]
		expected_normal = [1,0]
		self.assertEqual(graph._get_normal(*vectors),expected_normal)

	def test_unit_vectors_in_negative_y_direction(self):
		vectors = [(0,-1),(0,-1)]
		expected_normal = [-1,0]
		self.assertEqual(graph._get_normal(*vectors),expected_normal)

	def test_first_vector_in_positive_second_in_negative_y_direction(self):
		vectors = [(0,1),(0,-1)]
		expected_normal = [0,1]
		self.assertEqual(graph._get_normal(*vectors),expected_normal)

	def test_first_vector_in_positive_x_and_second_in_positive_y(self):
		vectors = [(1,0),(0,1)]
		expected_normal = [0.5*math.sqrt(2), -0.5*math.sqrt(2)]
		normal = graph._get_normal(*vectors)
		self.assertAlmostEqual(normal[0],expected_normal[0],delta=1e-10)
		self.assertAlmostEqual(normal[1],expected_normal[1],delta=1e-10)

	def test_aligned_vectors(self):
		n_of_tested_vals = 16
		for i in range(n_of_tested_vals):
			angle = math.pi*i/n_of_tested_vals
			e = (math.cos(angle), math.sin(angle))
			vectors = [e,e]
			expected_normal = [e[1],-e[0]]
			normal = graph._get_normal(*vectors)
			self.assertAlmostEqual(normal[0], expected_normal[0],delta=1e-08)
			self.assertAlmostEqual(normal[1], expected_normal[1],delta=1e-08)

		
if __name__=="__main__":
    unittest.main()