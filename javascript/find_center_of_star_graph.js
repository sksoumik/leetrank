// https://leetcode.com/problems/find-center-of-star-graph
// There is an undirected star graph consisting of n nodes labeled from 1 to n.
// A star graph is a graph where there is one center node
// and exactly n - 1 edges that connect the center node with every other node.
// You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates
// that there is an edge between the nodes ui and vi. Return the center of the given star graph.

/**
 * @param {number[][]} edges
 * @return {number}
 */

var findCenter = function (edges) {
  // find the intersection of all the arrays in edges
  // the intersection will be the center of the star graph
  let intersection = edges[0];
  for (let i = 1; i < edges.length; i++) {
    intersection = intersection.filter((x) => edges[i].includes(x));
  }
  return intersection[0];
};

console.log(
  findCenter([
    [1, 2],
    [2, 3],
    [4, 2],
  ])
);
