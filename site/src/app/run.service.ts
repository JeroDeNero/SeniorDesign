import { Injectable } from '@angular/core';

import { Observable, of } from 'rxjs';

import { Run } from './run';
import { RUN } from './mock-run';

@Injectable({
  providedIn: 'root'
})

export class RunService {

  constructor() { }

  getRuns(): Observable<Run> {
    return of(RUN)
  }
}
