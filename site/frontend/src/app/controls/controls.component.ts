import { Component, HostListener, OnInit } from '@angular/core';
import { AppComponent } from '../app.component';
import { StreamService } from '../stream.service';

@Component({
  selector: 'app-controls',
  templateUrl: './controls.component.html',
  styleUrls: ['./controls.component.css'],
})
export class ControlsComponent implements OnInit {
  private movementEnum = Object.freeze({
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

  private motionEnum = Object.freeze({
    'pos 1': 'forward',
    'neg 0': 'left',
    'pos 0': 'right',
    'neg 1': 'back',
    7: 'forward',
    4: 'left',
    5: 'right',
    6: 'back',
    12: 'forward',
    14: 'left',
    15: 'right',
    13: 'back',
  });

  private lastPressed: String = '';

  @HostListener('document:keydown', ['$event'])
  handleKeyboardPress(event: KeyboardEvent) {
    console.log(event);
    if (!event.repeat) {
      if (event.key !== this.lastPressed) {
        this.lastPressed = event.key;

        try {
          const action: String = this.movementEnum[event.key];

          if (event.key.includes('arrow')) {
            this.onCamClickD(action);
          } else if (action.includes('speed')) {
            //call speed function
          } else if (action === 'binary') {
            this.onBinClick();
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
      const action: String = this.movementEnum[event.key];

      if (event.key.includes('arrow')) {
        this.onCamClickD(action);
      } else if (action.includes('speed')) {
        //call speed function
      } else if (action === 'binary') {
        this.onBinClick();
      } else if (action === ' capture') {
        this.caputerImage();
      } else if (action) {
        this.onCamClickD(action);
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
      }, 500);
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
  lastButton: number = 2;

  gamepadInterval;
  intervalRunning: boolean = false;
  binaryOn: boolean = false;
  gamepads: Gamepad[] = [];
  slider: number = 50;

  constructor(
    private app: AppComponent,
    private streamService: StreamService
  ) {}

  ngOnInit(): void {
    this.setMovementStates();

    // get speed from python
  }

  setMovementStates() {
    this.movementState = {
      forward: false,
      backward: false,
      left: false,
      right: false,
    };
  }

  onClick(button) {
    // TODO call server, if the server could return set speed that would be perfect.
  }

  onClickD(button) {
    //TODO contact server with button (if the server could return true on sucessfully recieving info)
  }

  onClickR(button) {
    if (!this.movementState[button]) {
      //TODO contact server with button
      this.movementState[button] = false;
    }
  }

  onCamClickD(button) {
    //TODO contact server with button (if the server could return true on sucessfully recieving info)
  }

  onCamClickR(button) {
    if (!this.movementState[button]) {
      //TODO contact server with button
      this.movementState[button] = false;
    }
  }

  onBinClick() {
    //Send to backend
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
    console.log(this.gamepads);
  }

  removeGamepad(gamepad: Gamepad) {
    this.gamepads.splice(gamepad.index, 1, null);
    console.log(this.gamepads);
  }

  updateStatus() {
    if (this.intervalRunning) {
      this.scanGamepads();
    }

    this.gamepads.forEach((gamepad: Gamepad) => {
      console.log(gamepad.buttons);
      console.log(gamepad.axes);

      if (gamepad.buttons[2].value > 0 || gamepad.buttons[2].pressed) {
        //Call stop function
      } else {
        if (
          gamepad.buttons[this.lastButton].value > 0 ||
          gamepad.buttons[this.lastButton].pressed
        ) {
          //do nothing
        } else {
          const target = this.checkMotion(gamepad);
          if (target === 10) {
            let axis = [0, 0];

            axis[0] = gamepad.axes[0];
            axis[1] = gamepad.axes[1];

            const index =
              axis[0] === Math.max(Math.abs(axis[0]), Math.abs(axis[1]))
                ? 0
                : 1;
            const sign = axis[index] < 0 ? 'neg' : 'pos';

            this.socketEmit(
              'move',
              this.motionEnum[sign + ' ' + index],
              Math.abs(axis[index])
            );
          }
        }

        //TODO camera movement

        if (gamepad.buttons[0].value > 0 || gamepad.buttons[0].touched) {
          this.caputerImage();
        }

        if (
          !this.binaryOn &&
          (gamepad.buttons[1].value < 0 || gamepad.buttons[1].touched)
        ) {
          this.socketEmit('binary', 'on');
        } else if (
          this.binaryOn &&
          gamepad.buttons[1].value === 0 &&
          !gamepad.buttons[1].touched
        ) {
          this.socketEmit('binary', 'off');
        }
      }
    });
  }

  checkMotion(gp: Gamepad) {
    for (let i = 4; i < 8; i++) {
      if (gp.buttons[i].value > 0.049 || gp.buttons[i].pressed) {
        return i;
      }
    }
    /*
    for (let i = 12; i < 16; i++) {
      if((gp.buttons[i].value > 0.049 || gp.buttons[i].pressed)){
        return i;
      }
    }*/
    return 10;
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
      //socketEmit(stop)
    } else if (channel === 'move') {
      const speed = args || args <= 0 ? args : 1;
      //socketEmit(channel, {command : command, speed : speed})
    } else if (channel === 'camera') {
      //socketEmit CameraInfo
    } else if (channel === 'binary') {
      //socketEmit(binary, status)
    }
  }

  refocus() {
    this.streamService.refocus();
  }
}

interface Ihash {
  [key: string]: boolean;
}
