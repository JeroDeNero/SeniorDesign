import { Component, ViewChild, HostListener } from '@angular/core';

import { ToggleService } from './toggle.service';
import { StreamService } from './stream.service';
import { FilterService } from './filter.service';
import { RunService } from './run.service';
import { SortService } from './sortService.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  @ViewChild('videoElement') videoElement: any;
  video: any;
  filter: string = 'Filter';
  alpha: string = 'A ↘ Z';
  date: string = 'Date ↓';
  newIsShown: boolean = false;
  editIsShown: boolean = false;
  showSettings: boolean = false;
  sideList: boolean = true;
  sort: boolean = false;
  pullOutBar: boolean = true;
  hideFilter: boolean = true;
  resetFilter: boolean = true;
  showFavorites: boolean;
  showNamed: boolean;
  showUnamed: boolean;
  title = 'site';
  operation: string;
  pullOutCont = '<===';
  innerWidth: any;
  primaryCam: any;
  videoSrc: string = null;

  IsPrimaryCamLoading: boolean = false;

  constructor(
    private toggleService: ToggleService,
    private streamService: StreamService,
    private filterService: FilterService,
    private runService: RunService,
    private sortService: SortService
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

    this.streamService.captureReturn().subscribe((data) => {
      this.runService.addTag(data);
    });

    this.toggleService.getShowFavorites().subscribe((value) => {
      this.showFavorites = value;
    });

    this.toggleService.getShowNamed().subscribe((value) => {
      this.showNamed = value;
    });

    this.toggleService.getShowUnamed().subscribe((value) => {
      this.showUnamed = value;
    });

    this.toggleService.getResetFilter().subscribe((value) => {
      this.resetFilter = value;
    });

    this.toggleService.getVideo().subscribe((value) => {
      this.videoSrc = value;
    });

    this.toggleService.getShowSettings().subscribe((state) => {
      this.showSettings = state;
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

  toggleShowFilter() {
    this.hideFilter = !this.hideFilter;
    if (this.filter == 'Filter') {
      this.filter = 'Filter ✔';
    } else {
      this.filter = 'Filter';
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

  toggleSettings() {
    this.toggleService.toggleShowSettings();
  }

  search(targ) {
    this.filterService.search(targ);
  }

  reset() {
    this.filterService.reset();
    this.toggleService.toggleResetFilter();
  }
  closeRewatch(){
    this.toggleService.setVideo(null);
  }

  toggleSort() {
    this.sort = !this.sort;
  }

  sortAlpha() {
    if (this.alpha.includes('A ↘ Z')) {
      this.alpha = 'A ↗ Z•';
      this.sortService.sortString(this.runService.allRunsData, 'Name', true);
    } else {
      this.alpha = 'A ↘ Z•';
      this.sortService.sortString(this.runService.allRunsData, 'Name', false);
    }

    this.date = 'Date ↓';
  }

  sortDate() {
    if (this.date.includes('Date ↓')) {
      this.date = 'Date ↑•';
      this.sortService.sortNoneString(
        this.runService.allRunsData,
        'DateTaken',
        true
      );
    } else {
      this.date = 'Date ↓•';
      this.sortService.sortNoneString(
        this.runService.allRunsData,
        'DateTaken',
        false
      );
    }

    this.alpha = 'A ↘ Z';
  }
}
