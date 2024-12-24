// if statement

if (time < 10) {
  greeting = "Good morning";
} else if (time < 20) {
  greeting = "Good day";
} else {
  greeting = "Good evening";
}

// loops

for (let i = 0; i < 5; i++) {
  console.log("Hello World!");
}

const numbers = [1, 2, 3, 4, 5];

for (const number of numbers) {
  console.log(number);
}

function rectangle_area(height, width) {
    return height * width;
}
function square_area(length) {
    return length * length;
}
function circle_area(){
    return null
}
function right_triangle_area(){
    return null
}

console.log(Math.PI)