const linearSearch = (array, value) => {
  // linear search - takes in array, searches for value
  // one element at a time. If found, returns index of element,
  // otherwise returns -1
  for (i = 0; i < array.length; i++)
    if (array[i] == value) {
      return i
    }
  return -1
}


/* TEST CASES */
//linearSearch([57, 'star', 'i', 0, 230, 'five'], 57)
// return 0
//linearSearch([57, 'star', 'i', 0, 230, 'five'], 'i')
// return 2
//linearSearch([57, 'star', 'i', 0, 230, 'five'], 5)
// return -1
// linearSearch([], 0)
// return -1
