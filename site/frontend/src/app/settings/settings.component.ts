import { Component, OnInit } from '@angular/core';
import { RunService } from '../run.service';
import { ToggleService } from '../toggle.service';

@Component({
  selector: 'app-settings',
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css'],
})
export class SettingsComponent implements OnInit {
  wheelRaduis: number = 6;
  mainCameraFPS: number = 30;
  backCameraFPS: number = 30;

  showSettings: boolean;

  constructor(
    private runService: RunService,
    private toggleService: ToggleService
  ) {}

  ngOnInit(): void {
    //need to pull the .env varaiables for these settings
    this.toggleService.getShowSettings().subscribe((state) => {
      this.showSettings = state;
    });
  }

  comfirmBut(wheelRad, mainCamFPS, backCamFPS) {}

  cancelBut() {
    this.toggleService.setShowSettings(false);
  }
}
