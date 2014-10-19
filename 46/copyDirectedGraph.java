package test;

import java.util.ArrayList;
import java.util.HashMap;
//import java.util.HashSet;
import java.util.List;
import java.util.Map;
//import java.util.Set;

class GraphNode {
	public int data;
	public List<GraphNode> neighbors;
	public GraphNode(int data) {
		this.data = data;
		neighbors = new ArrayList<GraphNode>();
	}
}

public class copyDirectedGraph {
	public GraphNode copy(GraphNode node){
		if (node==null) {
			return null;
		}
		GraphNode first = new GraphNode(node.data);
		Map<GraphNode,GraphNode> visited = new HashMap<GraphNode,GraphNode>();
		visited.put(node, first);
		doGraphCopy(node,first,visited);
		return first;
		
	}

	private void doGraphCopy(GraphNode node, GraphNode ret,
			Map<GraphNode,GraphNode> visited) {
		for (GraphNode n :node.neighbors) {
			if (!visited.containsKey(n)) {
				GraphNode tmp = new GraphNode(n.data);
				ret.neighbors.add(tmp);
				if (n.neighbors.contains(node)) {
					tmp.neighbors.add(ret);
				}
				visited.put(n, tmp);
				doGraphCopy(n,tmp,visited);
				
			} else {
				ret.neighbors.add(visited.get(n));
				if (n.neighbors.contains(node)) {
					visited.get(n).neighbors.add(ret);
				}
			}
		}
		
	}

}
