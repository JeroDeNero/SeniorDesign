import { Component, ViewChild, HostListener } from '@angular/core';
import { VideoService, loadBinaryResource } from './video.service';
import { DomSanitizer } from '@angular/platform-browser';
import { Observable } from 'rxjs';

import { ToggleService } from './toggle.service';
import { StreamService } from './stream.service';
import { FilterService } from './filter.service';

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
  primaryCam: any;

  IsPrimaryCamLoading: boolean = false;

  constructor(
    private videoService: VideoService,
    private toggleService: ToggleService,
    private filterService: FilterService
  ) {}

  ngOnInit() {
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
    this.streamService.watchVideo().subscribe((data) => {
      this.primaryCam = data;
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
}
