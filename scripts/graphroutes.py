#!/usr/bin/env python

from graphviz import Graph
import sys

config = {
    'font_name': 'Pragmata Pro',
    'font_size': '13',
    'node_shape': 'plaintext',
    'node_margin': '0.1',
    'edge_thickness': '1.5',
    'image_format': 'png',
    'output_filename': 'donk_routes',
    'node_color': '#000000',  # black
    'edge_color': '#0000ff',  # blue
    'background_color': '#dddddd'
}

if len(sys.argv) > 1:
    input_source = open(sys.argv[1])
elif not sys.stdin.isatty():
    input_source = sys.stdin
else:
    script_name = sys.argv[0]
    print(f"Usage: {script_name} <filename> or pass data via stdin",
          file=sys.stderr)
    sys.exit(1)

G = Graph('G', filename='network.gv', engine='neato')
G.attr(bgcolor=config['background_color'])
G.attr('node', fontcolor=config['node_color'])
G.attr('edge', color=config['edge_color'])

added_nodes, added_edges = set(), set()


def parse_connected_nodes(line):
    parts = (line.strip()
                .replace(' and ', ', ')
                .replace('connected to ', '').split(', '))
    return parts[0], parts[1:]


with input_source as file:
    for line in file:
        node, connected_nodes = parse_connected_nodes(line)

        if node not in added_nodes:
            G.node(node,
                   fontname=config['font_name'],
                   fontsize=config['font_size'],
                   shape=config['node_shape'],
                   margin=config['node_margin'])
            added_nodes.add(node)

        for connected_node in connected_nodes:
            if connected_node not in added_nodes:
                G.node(connected_node,
                       fontname=config['font_name'],
                       fontsize=config['font_size'],
                       shape=config['node_shape'],
                       margin=config['node_margin'])
                added_nodes.add(connected_node)

            edge = tuple(sorted((node, connected_node)))
            if edge not in added_edges:
                G.edge(*edge)
                added_edges.add(edge)

G.render(config['output_filename'], format='png')
