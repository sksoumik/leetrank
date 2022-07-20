// Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1,
// find all possible paths from node 0 to node n - 1 and return them in any order.

// The graph is given as follows: graph[i] is a list of all nodes you
// can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

/**
 * @param {number[][]} graph
 * @return {number[][]}
 */
var allPathsSourceTarget = function (graph) {
  const results = [];
  dfs(graph, 0, [], results);
  return results;
};

function dfs(graph, node, path, results) {
  if (node === graph.length - 1) {
    results.push(path.concat(node));
    return;
  }
  for (let i = 0; i < graph[node].length; i++) {
    dfs(graph, graph[node][i], path.concat(node), results);
  }
}

console.log(allPathsSourceTarget([[1, 2], [3], [3], []]));
