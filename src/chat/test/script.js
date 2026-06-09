
const websocket = new WebSocket("ws://127.0.0.1:8000/5/channel");


function sendMessage(event) {
  event.preventDefault()
  var input = document.getElementById('authInput')
  var message = input.value
  websocket.send({
    'type': 'message',
    'content': {
      'message': message
    }
  })
  input
}

function sendAuth(event) {
  event.preventDefault()
  var input = document.getElementById('authInput')
  var token = input.content
  websocket.send({
    'type': 'auth',
    'content': {
      'token': token
    }
  })
}

websocket.onmessage = function (event) {
  console.log(event.data)
}