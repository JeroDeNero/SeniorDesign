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
  newRun: Run;
  temp: Run;
  hideHTML: boolean;

  constructor(
    private runService: RunService,
    private toggleService: ToggleService
  ) {}

  ngOnInit(): void {
    this.toggleService.getHideNew().subscribe((value) => {
      this.hideHTML = value;
    });
    this.runService.getNewRun().subscribe((value) => {
      this.newRun = value;
    });
    this.temp = this.runService.createEmptyRun();
  }

  comfirmBut(name, driverName, pipeID, dir, lat, long) {
    this.temp.Name = name;
    this.temp.DriverName = driverName;
    this.temp.PipeID = pipeID;
    this.temp.Direction = dir;
    this.temp.Lat = lat;
    this.temp.Longi = long;
    this.temp.Tagged = 0;

    this.runService.setNewRun(this.temp);

    this.toggleService.operateNewWindow();
  }

  cancelBut() {
    this.toggleService.setButtonOp('New Run');
    this.toggleService.toggleHideNew();
  }
}
