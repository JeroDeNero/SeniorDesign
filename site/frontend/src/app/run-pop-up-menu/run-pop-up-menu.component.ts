import { Component, Injectable, OnInit } from '@angular/core';
import { ToggleService } from '../toggle.service';

import { Run } from '../interfaces';
import { RunService } from '../run.service';

@Injectable({
  providedIn: 'root',
})
@Component({
  selector: 'app-run-pop-up-menu',
  templateUrl: './run-pop-up-menu.component.html',
  styleUrls: ['./run-pop-up-menu.component.css'],
})
export class RunPopUpMenuComponent implements OnInit {
  newRun: Run = this.runService.createEmptyRun();
  hideHTML: boolean;

  constructor(
    private runService: RunService,
    private toggleService: ToggleService
  ) {}

  ngOnInit(): void {
    this.toggleService.getHideNew().subscribe((value) => {
      this.hideHTML = value;
    });
  }

  comfirmBut() {
    this.newRun.Id = -1;
    this.newRun.DateTaken = new Date();
    this.runService.addRun(this.newRun);
  }

  cancelBut() {
    this.toggleService.setButtonOp('New Run');
    this.toggleService.toggleHideNew();
  }
}
