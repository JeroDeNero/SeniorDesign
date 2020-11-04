import { Component, HostListener, OnInit } from '@angular/core';
import { Ihash } from '../interfaces';
import { Socket } from 'ngx-socket-io';
import { StreamService } from '../stream.service';
import { Controller } from '../classes';
import { emit } from 'process';

@Component({
  selector: 'app-controls',
  templateUrl: './controls.component.html',
  styleUrls: ['./controls.component.css'],
})
export class ControlsComponent implements OnInit {
  private lastPressed: String = '';

  @HostListener('document:keydown', ['$event'])
  handleKeyboardPress(event: KeyboardEvent) {
    console.log(event);
    if (!event.repeat) {
      if (event.key !== this.lastPressed) {
        this.lastPressed = event.key;

        try {
          const action: String = this.keyboardEnum[event.key];

          if (event.key.includes('arrow')) {
            this.onCamClickD(action);
          } else if (action.includes('speed')) {
            //call speed function
          } else if (action === 'binary') {
            this.onBinClick('True');
          } else if (action === ' capture') {
            this.caputerImage();
          } else if (action) {
            this.onCamClickD(action);
          }
        } catch {
          console.log("doesn't exist");
        }
      }
    }
  }

  @HostListener('document:keyup', ['$event'])
  handleKeyboardlift(event: KeyboardEvent) {
    try {
      const action: String = this.keyboardEnum[event.key];

      if (event.key.includes('arrow')) {
        this.onCamClickR(action);
      } else if (action === 'speedUp') {
        this.slider += 5;
        this.socketEmit('speed');
      } else if (action === 'speedDown') {
        this.slider -= 5;
        this.socketEmit('speed');
      } else if (action === 'binary') {
        this.onBinClick('False');
      } else if (action) {
        this.onCamClickR(action);
      }
    } catch {
      console.log("doesn't exist");
    }
  }

  @HostListener('window:gamepadconnected', ['$event'])
  handleControllerConnect(event) {
    this.addGamepad(event.gamepad);
    if (!this.intervalRunning) {
      this.gamepadInterval = setInterval(() => {
        this.updateStatus();
      }, 750);
    }
  }

  @HostListener('window:gamepaddisconnected', ['$event'])
  handleControllerDisconnected(event) {
    this.removeGamepad(event);
    if (this.gamepads.every((item) => item === null)) {
      clearInterval(this.gamepadInterval);
    }
    console.log('Gamepad disconnected');
  }

  movementState: Ihash;
  camState: Ihash;

  gamepadInterval;
  intervalRunning: boolean = false;
  gamepads: Gamepad[] = [];
  controllers: Controller[] = [];
  prevControllers: Controller[] = [];
  slider: number = 50;

  constructor(private socket: Socket, private streamService: StreamService) {}

  ngOnInit(): void {
    // get speed from python
  }

  setMovementStates() {
    this.movementState = {
      forward: 0,
      backward: 0,
      left: 0,
      right: 0,
    };
  }

  onClickD(button) {
    this.setMovementStates;
    this.movementState[button] = this.slider;

    if (button === 'left') {
      this.socketEmit('movement', 'turn', this.slider * -1);
    } else if (button === 'right') {
      this.socketEmit('movement', 'turn', this.slider);
    } else if (button === 'back') {
      this.socketEmit('movement', 'straight', this.slider * -1);
    } else {
      this.socketEmit('movement', 'straight', this.slider);
    }
  }

  onClickR(button) {
    if (!this.movementState[button]) {
      this.movementState[button] = 0;

      if (button === 'left' || button === 'right') {
        this.socketEmit('movement', 'turn', 0);
      } else {
        this.socketEmit('movement', 'straight', 0);
      }
    }
  }

  onCamClickD(button) {
    if (button === 'left') {
      this.socketEmit('movement', 'turn', this.slider * -1);
    } else if (button === 'right') {
      this.socketEmit('movement', 'turn', this.slider);
    }
    if (button === 'down') {
      this.socketEmit('movement', 'straight', this.slider * -1);
    } else {
      this.socketEmit('movement', 'straight', this.slider);
    }
  }

  onCamClickR(button) {
    if (!this.movementState[button]) {
      this.movementState[button] = 0;

      if (button === 'left' || button === 'right') {
        this.socketEmit('camera', 'x', 0);
      } else {
        this.socketEmit('camera', 'y', 0);
      }
    }
  }

  onBinClick(state) {
    this.socketEmit('binary', state);
  }

  caputerImage() {
    this.streamService.captureImage();
  }

  addGamepad(gamepad: Gamepad) {
    console.log(gamepad);
    try {
      this.gamepads[gamepad.index] = gamepad;
    } catch {
      this.gamepads.push(gamepad);
    }
  }

  removeGamepad(gamepad: Gamepad) {
    this.gamepads.splice(gamepad.index, 1, null);
    console.log(this.gamepads);
  }

  updateStatus() {
    if (this.intervalRunning) {
      this.scanGamepads();
    }

    this.gamepads.forEach((gamepad: Gamepad, index) => {
      if (!this.controllers[index]) {
        this.controllers.push(new Controller(gamepad));
      } else if (gamepad.timestamp === this.controllers[index].timestamp) {
        return;
      } else {
        this.prevControllers[index] = this.controllers[index];
        this.controllers[index].updateController(gamepad);
      }

      if (this.controllers[index].buttons[5] > 0) {
        if (
          this.controllers[index].buttons[5] !==
          this.prevControllers[index].buttons[5]
        ) {
          this.socketEmit('stop');
        }
        return;
      }

      if (
        this.controllers[index].buttons[4] !==
          this.prevControllers[index].buttons[4] &&
        this.controllers[index].buttons[4]
      ) {
        this.streamService.captureImage();
      }

      if (
        this.controllers[index].buttons[11] !==
          this.prevControllers[index].buttons[11] &&
        this.controllers[index].buttons[11]
      ) {
        this.streamService.refocus();
      }

      if (
        this.controllers[index].buttons[7] !==
          this.prevControllers[index].buttons[7] &&
        this.controllers[index].buttons[7]
      ) {
        this.socketEmit('binary', 'True');
      } else if (
        this.controllers[index].buttons[7] !==
        this.prevControllers[index].buttons[7]
      ) {
        this.socketEmit('binary', 'False');
      }

      if (
        this.controllers[index].axes[0] !==
          this.prevControllers[index].axes[0] &&
        this.controllers[index].axes[0] &&
        this.controllers[index].axes[0] >= this.controllers[index].axes[1]
      ) {
        this.socketEmit('movement', 'turn', this.controllers[index].axes[0]);
      } else if (
        this.controllers[index].axes[1] !==
          this.prevControllers[index].axes[1] &&
        this.controllers[index].axes[1] &&
        this.controllers[index].axes[1] >= this.controllers[index].axes[0]
      ) {
        this.socketEmit(
          'movement',
          'straight',
          this.controllers[index].axes[1]
        );
      }

      if (
        this.controllers[index].axes[2] !==
          this.prevControllers[index].axes[2] &&
        this.controllers[index].axes[2]
      ) {
        this.socketEmit('camera', 'x', this.controllers[index].axes[2]);
      }

      if (
        this.controllers[index].axes[3] !==
          this.prevControllers[index].axes[3] &&
        this.controllers[index].axes[3]
      ) {
        this.socketEmit('camera', 'y', this.controllers[index].axes[2]);
      }
    });
  }

  scanGamepads() {
    let gamepads: Gamepad[] = navigator.getGamepads
      ? navigator.getGamepads()
      : [];

    gamepads.forEach((gamepad: Gamepad) => {
      if (gamepad) {
        if (this.gamepads[gamepad.index]) {
          this.gamepads[gamepad.index] = gamepad;
        } else {
          this.addGamepad(gamepad);
        }
      }
    });
  }

  socketEmit(channel: string, command?: string, args?: Number) {
    if (channel === 'stop') {
      this.socket.emit(channel);
    } else if (channel === 'binary') {
      this.socket.emit(channel, command);
    } else if (channel === 'speed') {
      this.socket.emit(channel, this.slider);
    } else if (command) {
      const speed = args || args <= 0 ? args : 1;
      this.socket.emit(channel, { command: command, speed: speed });
    } else {
      this.socket.emit(command);
    }
  }

  private keyboardEnum = Object.freeze({
    w: 'forward',
    a: 'left',
    d: 'right',
    s: 'back',
    ArrowUp: 'Up',
    ArrowLeft: 'left',
    ArrowRight: 'right',
    ArrowDown: 'down',
    q: 'binaryAct',
    e: 'capture',
    r: 'speedUp',
    f: 'speedDown',
  });
}
