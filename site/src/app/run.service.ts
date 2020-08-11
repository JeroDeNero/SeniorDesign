import { Injectable } from '@angular/core';

import { Observable, of } from 'rxjs';

import { Run, Tag } from './run';
import { RUNS } from './mock-run';

@Injectable({
  providedIn: 'root'
})

export class RunService {

  constructor() { }

  getFavRuns(): Observable<Run[]> {
    return of(RUNS)
  }

  getNamedRuns(): Observable<Run[]> {
    return of(RUNS)
  }

  getUnNamedRuns(): Observable<Run[]> {
    return of(RUNS)
  }

  getRun(id: number): Observable<Run> {
    return of(RUNS.find(run => run.videoID === id))
  }
}
