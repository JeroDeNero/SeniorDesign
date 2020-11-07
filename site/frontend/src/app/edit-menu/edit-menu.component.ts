import { Component, Injectable, OnInit } from '@angular/core';

import { Run } from '../interfaces';
import { RunService } from '../run.service';
import { ToggleService } from '../toggle.service';

@Injectable({
  providedIn: 'root',
})
@Component({
  selector: 'app-edit-menu',
  templateUrl: './edit-menu.component.html',
  styleUrls: ['./edit-menu.component.css'],
})
export class EditMenuComponent implements OnInit {
  hideHTML: boolean;
  targRun: Run;

  constructor(
    private runService: RunService,
    private toggleService: ToggleService
  ) {}

  ngOnInit(): void {
    this.runService.getEditRun().subscribe((value) => (this.targRun = value));
    this.toggleService.getHideEdit().subscribe((value) => {
      this.hideHTML = value;
    });
  }

  comfirmBut(name, driverName, pipeID, dir, lat, long) {
    this.targRun.Name = name;
    this.targRun.DriverName = driverName;
    this.targRun.PipeID = pipeID;
    this.targRun.Direction = dir;
    this.targRun.Lat = lat;
    this.targRun.Longi = long;

    this.runService.setEditRun(this.targRun);
    this.runService.updateRun().subscribe();
    alert('Updated Run');
    this.toggleService.toggleHideEdit();
  }

  cancelBut() {
    this.toggleService.toggleHideEdit();
  }
}
