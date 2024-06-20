const laneCount = Math.floor(Math.random() * 3) + 3;

const carCanvas = document.getElementById("carCanvas");
carCanvas.width = 50 * laneCount;
const networkCanvas = document.getElementById("networkCanvas");
networkCanvas.width = 500;

const carCtx = carCanvas.getContext("2d");
const networkCtx = networkCanvas.getContext("2d");

const road = new Road(carCanvas.width/2, carCanvas.width * 0.9, laneCount);

const N = 500;
const cars = generateCars(N);
let bestCar = cars[0];
if (localStorage.getItem("bestBrain")){
  for (let i = 0; i < cars.length; i++){
    cars[i].brain = JSON.parse(
      localStorage.getItem("bestBrain"));
    if (i != 0){
      NeuralNetwork.mutate(cars[i].brain, 0.2);
    }
  }
}

const traffic = [
  new Car(road.getLaneCenter(1), -100, 30, 50, "DUMMY", 5),
  new Car(road.getLaneCenter(0), -500, 30, 50, "DUMMY", 5),
  new Car(road.getLaneCenter(2), -500, 30, 50, "DUMMY", 5),
];

let nextTrafficCar = 3;

animate();

function save(){
  localStorage.setItem("bestBrain",
    JSON.stringify(bestCar.brain));
}

function discard(){
  localStorage.removeItem("bestBrain");
}

function generateCars(N){
  const cars = [];
  for (let i = 1; i <= N; i++){
    cars.push(new Car(road.getLaneCenter(1), 100, 30, 50, "AI"));
  }
  return cars;
}

function animate(time){
  if (time >= nextTrafficCar * 1000){
    const randLane = Math.round(Math.random() * road.laneCount);
    const newTraffic = new Car(road.getLaneCenter(randLane), bestCar.y - carCanvas.height, 30, 50, "DUMMY", 5);
    traffic.push(newTraffic);

    let openLane = Math.floor(Math.random() * road.laneCount);
    while (openLane == randLane){
      openLane = Math.floor(Math.random() * road.laneCount);
    }

    for (let i = 0; i < road.laneCount; i++){
      if (i == openLane || i == randLane) continue;
      if (Math.random() > .3){
        const extraTraffic = new Car(road.getLaneCenter(i), bestCar.y - carCanvas.height, 30, 50, "DUMMY", 5);
        traffic.push(extraTraffic);
      }
    }

    nextTrafficCar += Math.round(Math.random() * 3) + 2;
  }
  for (let i = 0; i < traffic.length; i++){
    traffic[i].update(road.borders, []);
  }

  for (let i = 0; i < cars.length; i++){
    cars[i].update(road.borders, traffic, road);
  }
  bestCar = cars.find(
    c=>c.score == Math.max(
      ...cars.map(c=>c.score)
    ));
  
  carCanvas.height = window.innerHeight;
  networkCanvas.height = window.innerHeight;

  carCtx.save();
  carCtx.translate(0, -bestCar.y + carCanvas.height*0.7);

  road.draw(carCtx);
  for (let i = 0; i < traffic.length; i++){
    traffic[i].draw(carCtx, "red");
  }
  
  carCtx.globalAlpha = 0.2;
  for (let i = 0; i < cars.length; i++){
    cars[i].draw(carCtx, "blue");
  }
  carCtx.globalAlpha = 1;
  bestCar.draw(carCtx, "blue", true);

  document.getElementById('score').textContent = "Score: " + (bestCar.score / 1000).toFixed(2);

  carCtx.restore();

  networkCtx.lineDashOffset = -time / 50;
  Visualizer.drawNetwork(networkCtx, bestCar.brain);
  requestAnimationFrame(animate);
}