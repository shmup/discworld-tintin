#!/usr/bin/env python

from graphviz import Graph

font_name = 'Pragmata Pro'
font_size = '13'
node_shape = 'plaintext'
node_margin = '0.1'
edge_thickness = '1.5'
image_format = 'png'
output_filename = 'donkroutes'
node_color = 'black'
edge_color = 'blue'
background_color = '#dddddd'

G = Graph('G', filename='network.gv', engine='neato')
G.attr(bgcolor=background_color)
G.attr('node', fontcolor=node_color)
G.attr('edge', color=edge_color)

added_nodes = set()
added_edges = set()

with open('rls.txt', 'r') as file:
    for line in file:
        parts = line.strip().replace(' and ',
                                     ', ').replace('connected to ',
                                                   '').split(', ')
        main_node = parts[0]
        connected_nodes = parts[1:]

        if main_node not in added_nodes:
            G.node(main_node,
                   fontname=font_name,
                   fontsize=font_size,
                   shape=node_shape,
                   margin=node_margin)
            added_nodes.add(main_node)

        for connected_node in connected_nodes:
            if connected_node not in added_nodes:
                G.node(connected_node,
                       fontname=font_name,
                       fontsize=font_size,
                       shape=node_shape,
                       margin=node_margin)
                added_nodes.add(connected_node)

            edge = tuple(sorted((main_node, connected_node)))

            if edge not in added_edges:
                G.edge(*edge)
                added_edges.add(edge)

G.render('donkroutes', format='png', view=False)
