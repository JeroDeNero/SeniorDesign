import { Component, OnInit } from '@angular/core';
import { AppComponent } from '../app.component';

import { Run } from '../run';
import { RunService } from '../run.service'

@Component({
  selector: 'app-run-pop-up-menu',
  templateUrl: './run-pop-up-menu.component.html',
  styleUrls: ['./run-pop-up-menu.component.css']
})
export class RunPopUpMenuComponent implements OnInit {

  run: Run;

  constructor(
    private app: AppComponent,
    private runService: RunService
  ) { }

  ngOnInit(): void {
    this.getRun();
  }

  getRun() {
    this.runService.getRuns()
      .subscribe(run => this.run = run);
  }

  toggleShow() {
    this.app.toggleShow();
  }

}
