const selectionSort = (array) => {
  for (let i = 0; i < array.length-1; i++) {
    let minIndex = i
    for (let j = i; j < array.length; j++) {
      if (array[j] < array[minIndex]) {
        minIndex = j
      }
    }
    let temp = array[i]
    array[i] = array[minIndex]
    array[minIndex] = temp
  }
  return array
}

selectionSort([3, 4, 2, 7, 1])

// takes in unsorted array
// create min value starting at index 0 of unsorted array
// create start value at index 0 of unsorted array
// go through unsorted array to find new min value.
// swap min with array at index 0
//
