import { Injectable } from '@angular/core';
import { filter } from 'rxjs/operators';
import { Run } from './interfaces';
import { RunService } from './run.service';
import { ToggleService } from './toggle.service';

@Injectable({
  providedIn: 'root',
})
export class FilterService {
  filtered: boolean = false;

  constructor(
    private toggleService: ToggleService,
    private runService: RunService
  ) {
    this.runService.getAllRuns().subscribe((data) => {
      this.runService.allRunsData = data;
    });
  }

  reset() {
    this.runService.allRunsData.forEach((runs) => {
      runs.forEach((run) => {
        run.ShowRun = true;
      });
    });
    this.toggleService.setShowFavorites(true);
    this.toggleService.setShowNamed(true);
    this.toggleService.setShowUnamed(true);
  }

  search(targ) {
    this.runService.allRunsData.forEach((runs) => {
      runs.forEach((run) => {
        if (run.Name.toString().includes(targ)) {
          run.ShowRun = true;
        } else if (!this.filtered) {
          run.ShowRun = false;
        }
      });
    });
  }

  showFavorites(value) {
    this.toggleService.setShowFavorites(value);
  }

  showNamed(value) {
    this.toggleService.setShowNamed(value);
  }

  showUnamed(value) {
    this.toggleService.setShowUnamed(value);
  }

  showProblems(_all, _low, _mid, _high) {
    //type is severity of the problem, this is not currently tracked on the yet though
    this.runService.allRunsData.forEach((runs) => {
      runs.forEach((run) => {
        if (run.tag && run.tag.length < 1) {
          run.ShowRun = false;
        }
      });
    });
  }

  showArea(long, lat, raduis) {
    const coordsA = { long: long / Math.PI, lat: lat / Math.PI };
    const earthRaduis = 20902000; //In feet I think

    this.runService.allRunsData.forEach((runs) => {
      runs.forEach((run) => {
        const coordsB = {
          long: run.Longi.valueOf() / Math.PI,
          lat: run.Lat.valueOf() / Math.PI,
        };
        const longDif = coordsA.long - coordsB.long;
        const latDif = coordsA.lat - coordsB.lat;
        const a =
          Math.pow(Math.sin(latDif / 2), 2) +
          Math.cos(coordsA.lat) *
            Math.cos(coordsB.lat) *
            Math.pow(Math.sin(longDif / 2), 2);

        const c = 2 * Math.asin(Math.sqrt(a));
        const distance = c * earthRaduis;
        if (distance > raduis) {
          run.ShowRun = false;
        }
      });
    });
  }

  showDate(from, to?) {
    if (!to) {
      to = new Date();
    }

    this.runService.allRunsData.forEach((runs) => {
      runs.forEach((run) => {
        if (run.DateTaken.valueOf() < from || run.DateTaken.valueOf() < to) {
          run.ShowRun = false;
        }
      });
    });
  }

  showOperator(name) {
    this.runService.allRunsData.forEach((runs) => {
      runs.forEach((run) => {
        if (run.DriverName !== name) {
          run.ShowRun = false;
        }
      });
    });
  }
}
