import { Component, ViewChild, HostListener } from '@angular/core';
import { VideoService, loadBinaryResource } from './video.service';
import { Observable } from 'rxjs';

import { ToggleService } from './toggle.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  @ViewChild('videoElement') videoElement: any;
  video: any;
  newIsShown: boolean = false;
  editIsShown: boolean = false;
  sideList: boolean = true;
  pullOutBar: boolean = true;
  title = 'site';
  operation: string;
  pullOutCont = '<===';
  innerWidth: any;
  primaryCam;

  constructor(
    private videoService: VideoService,
    private toggleService: ToggleService
  ) {}

  ngOnInit() {
    this.primaryCam = this.getVideo;
    this.innerWidth = window.innerWidth;

    if (this.innerWidth < 1775) {
      this.sideList = false;
      this.pullOutBar = true;
    } else {
      this.sideList = true;
      this.pullOutBar = false;
    }

    this.toggleService.getButtonOp().subscribe((value) => {
      this.operation = value;
    });
  }

  @HostListener('window:resize', ['$event'])
  onResize(event) {
    this.innerWidth = window.innerWidth;

    if (this.innerWidth < 1775 && !this.pullOutBar) {
      this.pullOutBar = true;
    } else if (this.innerWidth >= 1775 && this.pullOutBar) {
      this.pullOutBar = false;
    }

    if (this.innerWidth < 1775 && this.sideList) {
      this.sideList = false;
    } else if (this.innerWidth >= 1775 && !this.sideList) {
      this.sideList = true;
    }
  }

  toggleNewMenu() {
    this.toggleService.operateNewWindow();
  }

  toggleSideMenu() {
    this.sideList = !this.sideList;

    if (this.pullOutCont === '<===') {
      this.pullOutCont = 'X';
    } else {
      this.pullOutCont = '<===';
    }
  }

  toggleNewShow() {
    this.newIsShown = !this.newIsShown;
  }

  fillData(runID) {
    if (runID === null) {
      return;
    } else if (runID === 'newRun') {
    }
  }

  getVideo(): Observable<any> {
    return <any>loadBinaryResource();
  }
}
