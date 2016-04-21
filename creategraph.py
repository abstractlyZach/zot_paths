# create graph file

write_file_name = input('Enter name of the file to write to: ')
ring_road_max = int(input('Enter the number of the largest Ring Road node: '))
aldrich_park_max = int(input('Enter the number of the largest Aldrich Park node: '))
with open(write_file_name, 'w') as write_file:
	for node_number in range(ring_road_max):
		write_file.write('RR{:02} '.format(node_number + 1))
	for node_number in range(aldrich_park_max):
		write_file.write('AP{:02} '.format(node_number + 1))
	write_file.write('\n')

	edge_input = input('Enter edge information ("q" to quit): ')
	edge_info = ''
	while edge_input != 'q':
		to_add = edge_input
		edge_input = input('Enter edge information ("q" to quit): ')
		if 'undo' != edge_input and 'undo' != to_add: # allows for undoing the previous line
			edge_info += to_add + '\n'

	write_file.write(edge_info)
