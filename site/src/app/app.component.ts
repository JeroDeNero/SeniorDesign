import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  isShown: boolean = false;
  title = 'site';

  toggleShow() {
    this.isShown = !this.isShown;
  }

  fillData(runID) {
    if (runID === null) {
      return;
    } else if (runID === "newRun") {

    }
  }
}
