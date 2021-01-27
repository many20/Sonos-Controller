//import {PythonShell} from 'python-shell';
const { PythonShell } = require('python-shell');
const { EventEmitter } = require('events');

const createKeyboardHooks = () => {
  const events = new EventEmitter();
  const pyshell = new PythonShell('text2.py', { pythonOptions: ['-u'] });

  // sends a message to the Python script via stdin
  //pyshell.send('hello');

  pyshell.send(
    JSON.stringify([
      ['0', '0'],
      ['1', '1'],
      ['2', '2'],
      ['3', '3'],
      ['4', '4'],
      ['5', '5'],
      ['6', '6'],
      ['7', '7'],
      ['8', '8'],
      ['9', '9'],
      ['0', '0'],
      ['enter', 'enter'],
    ]),
  );

  let command = '';

  pyshell.on('message', function (message) {
    console.log(message);

    switch (message) {
      case 'hello':
        // received a message sent from the Python script (a simple "print" statement)
        //console.log(message);
        events.emit('hello');
        break;
      case 'ready':
        // received a message sent from the Python script (a simple "print" statement)
        //console.log(message);
        events.emit('ready');
        break;
      case '1':
      case '2':
      case '3':
      case '4':
      case '5':
      case '6':
      case '7':
      case '8':
      case '9':
      case '0':
        command += message;
        break;
      case 'enter':
        console.log(command);
        events.emit('command', command);
        command = '';
        break;
      default:
        break;
    }
  });

  // end the input stream and allow the process to exit
  pyshell.end(function (err, code, signal) {
    // if (err) throw err;
    // console.log('The exit code was: ' + code);
    // console.log('The exit signal was: ' + signal);
    // console.log('finished');
    events.emit('end', { err, code, signal });
  });

  return {
    events,
    terminate: () => {
      pyshell.kill();
    },
  };
};

const a = createKeyboardHooks();
//a.terminate();
