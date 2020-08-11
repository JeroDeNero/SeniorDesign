import { Component, OnInit } from '@angular/core';
import { AppComponent } from '../app.component';

@Component({
  selector: 'app-controls',
  templateUrl: './controls.component.html',
  styleUrls: ['./controls.component.css']
})


export class ControlsComponent implements OnInit {

  movementState: Ihash;

  constructor(private app: AppComponent) {
  }

  ngOnInit(): void {
    this.movementState["forward"] = false;
    this.movementState["backward"] = false;
    this.movementState["right"] = false;
    this.movementState["left"] = false;
  }

  onClick(button) {
    // TODO call server, if the server could return set speed that would be perfect.
  }

  onClickD(button) {
    window.alert("hi")
    //TODO contact server with button (if the server could return true on sucessfully recieving info)
    this.movementState[button] = true;
    window.alert(this.movementState[button])
  }

  onClickR(button) {
    if (this.movementState[button]) {
      //TODO contact server with button
      this.movementState[button] = false;
      window.alert(this.movementState[button])
    }
  }

}

interface Ihash {
  [key: string]: boolean;
}