import { Component, OnInit } from '@angular/core';
import { AppComponent } from '../app.component';
import { StreamService } from '../stream.service';

@Component({
  selector: 'app-controls',
  templateUrl: './controls.component.html',
  styleUrls: ['./controls.component.css'],
})
export class ControlsComponent implements OnInit {
  movementState: Ihash;

  constructor(
    private app: AppComponent,
    private streamService: StreamService
  ) {}

  ngOnInit(): void {
    this.setMovementStates();
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
    this.movementState[button] = true;
  }

  onClickR(button) {
    if (!this.movementState[button]) {
      //TODO contact server with button
      this.movementState[button] = false;
    }
  }

  caputerImage() {
    this.streamService.caputerImage();
  }
}

interface Ihash {
  [key: string]: boolean;
}
