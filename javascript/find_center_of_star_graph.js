
https://leetcode.com/problems/find-center-of-star-graph

// There is an undirected star graph consisting of n nodes labeled from 1 to n.
// A star graph is a graph where there is one center node
// and exactly n - 1 edges that connect the center node with every other node.
// You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates
// that there is an edge between the nodes ui and vi. Return the center of the given star graph.


/**
 * @param {number[][]} edges
 * @return {number}
 */
 var findCenter = function(edges) {
    // common element in all the arrays
    let common = edges[0][0];
    // create a map of the edges
    let map = new Map();
    // loop through the edges
    for (let i = 0; i < edges.length; i++) {
        

