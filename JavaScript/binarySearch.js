const binarySearch = (array, value) => {
  // binary search algorithm.
  // calls a recursive helper function to search for a value
  // the helper function takes in a array, a start index, and end index
  // and a value
  return binaryHelper(array, 0, array.length-1, value)
}
const binaryHelper = (array, start, end, value) => {
  // Recursive helper function to find value in a array
  // finds mid point of array, if it equals the value, the index
  // is returned.
  // if the mid point is larger than the value the function is called
  // again with the left side of the array.
  // if the mid point is smaller than the value, the function is called
  // again witht eh right side of the array.
  // if there is one element left in the array and it does not equal the
  // value, -1 is returned
  let mid = Math.floor((start+end)/2)
  if (end >= start) {
    if (array[mid] === value) {
      return mid
    } else if (array[mid] > value) {
        return binaryHelper(array, start, mid - 1, value)
    } else  {
        return binaryHelper(array, mid + 1, end, value)
    }
  } else {
    return -1
  }
}


/* TEST CASES */
// binarySearch([0, 3, 5, 12, 27, 29, 51], 0)       // return 0
binarySearch([0, 3, 5, 12, 27, 29, 51], 27)      // return 4
// binarySearch([0, 3, 5, 12, 27, 29, 51], 4)       // return -1
// binarySearch([0, 3, 5, 12, 27, 29], 3)           // return 1
// binarySearch([0, 3, 5, 12, 27, 29], 21)          // return -1
// binarySearch([4], 4)                             // return 0
// binarySearch([], 0)                              // return -1
