import { Injectable } from '@angular/core';

import { Observable, of } from 'rxjs';

import { Run, Tag } from './interfaces';
import { RUNS } from './mock-run';
import { isUndefined } from 'util';

@Injectable({
  providedIn: 'root'
})

export class RunService {

  constructor() { }

  getRuns(listType): Observable<Run[]> {
    return of(RUNS[listType])
  }

  flatIt(runs) {
    const initialVal = [];

    return runs.reduce((total, value) => {
      return total.concat(Array.isArray(value) ? this.flatIt(value) : value);
    }, initialVal);
  }

  getRun(id: number): Observable<Run> {
    return of(this.flatIt(RUNS).find(run => run.videoID === id));
  }
}
