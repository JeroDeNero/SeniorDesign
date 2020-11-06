import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { BehaviorSubject, Observable, Observer, of, Subject } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';

import { Run, Tag } from './interfaces';

import { API_URL } from './env';
import { DateHandlerService } from './date-handler.service';

@Injectable({
  providedIn: 'root',
})
export class RunService {
  private editRun: BehaviorSubject<Run> = new BehaviorSubject<Run>(
    this.createEmptyRun()
  );

  arrayIndex: number[];

  private newRun: BehaviorSubject<Run> = new BehaviorSubject<Run>(
    this.createEmptyRun()
  );

  newRunData: Run;

  private allRuns: BehaviorSubject<Run[][]> = new BehaviorSubject<Run[][]>([]);

  allRunsData: Run[][];

  constructor(
    private http: HttpClient,
    private dateHandlerService: DateHandlerService
  ) {
    this.getRuns().subscribe((data) => {
      this.setAllRuns(data);
    });

    this.getAllRuns().subscribe((data) => {
      this.allRunsData = data;
    });
  }

  /**
   * Handle Http operation that failed.
   * Let the app continue.
   * @param operation - name of the operation that failed
   * @param result - optional value to return as the observable result
   */

  private handleError<T>(result?: T) {
    return (error: any): Observable<T> => {
      console.log(error);

      return of(result as T);
    };
  }

  setAllRuns(data: Run[][]) {
    this.allRuns.next(data);
  }

  getAllRuns(): Observable<Run[][]> {
    return this.allRuns.asObservable();
  }

  addTag(tag: Tag): void {
    this.newRunData.tags.push(tag);
    console.log(this.newRunData);
  }

  setNewRun(run: Run): void {
    this.newRunData = run;
  }

  getNewRun(): Observable<Run> {
    return this.newRun.asObservable();
  }

  setEditRun(run: Run): void {
    if (run.Id !== this.editRun.getValue().Id) {
      this.editRun.next(run);
    }
  }

  getEditRun(): Observable<Run> {
    return this.editRun.asObservable();
  }

  getRuns(): Observable<Run[][]> {
    return this.http.get<Run[][]>(`http://${API_URL}/get/runs`).pipe(
      tap((_) => console.log('fetched runs')),
      catchError(this.handleError<Run[][]>([]))
    );
  }

  getRun(id: number): Observable<Run> {
    return this.http
      .post<Run>(`http://${API_URL}/get/run`, { id: id }, this.httpOptions)
      .pipe(
        tap((_) => console.log('fetched run')),
        catchError(this.handleError<Run>(null))
      );
  }

  flatIt(runs) {
    const initialVal = [];

    return runs.reduce((total, value) => {
      return total.concat(Array.isArray(value) ? this.flatIt(value) : value);
    }, initialVal);
  }

  addRun(): Observable<Run> {
    const runToAdd = this.newRunData;
    this.newRunData = this.createEmptyRun();

    let type = 2;

    if (runToAdd.Name && runToAdd.Tagged) {
      type = 0;
    } else if (runToAdd.Name) {
      type = 1;
    }

    console.log(runToAdd);

    return this.http
      .post<Run>(`http://${API_URL}/save/newRun`, runToAdd, this.httpOptions)
      .pipe(
        tap(() => {
          console.log('added run');
          this.allRunsData[type].unshift(runToAdd);
        }),
        catchError(this.handleError<Run>())
      );
  }

  updateRun(): Observable<any> {
    this.allRunsData[this.arrayIndex[0]][
      this.arrayIndex[1]
    ] = this.editRun.getValue();

    return this.http
      .post(
        `http://${API_URL}/save/editRun`,
        this.editRun.getValue(),
        this.httpOptions
      )
      .pipe(
        tap((_) =>
          console.log(`updated run id =${this.editRun.getValue().Id}`)
        ),
        catchError(this.handleError<any>())
      );
  }

  changePin(run: Run): Observable<any> {
    return this.http
      .post(
        `http://${API_URL}/save/editPin`,
        { id: run.Id, tagged: run.Tagged },
        this.httpOptions
      )
      .pipe(
        tap((_) => console.log(`updated run id =${run.Id}`)),
        catchError(this.handleError<any>())
      );
  }

  deleteRun(run: Run | number, date: Date, pipeID: String): Observable<any> {
    const id = typeof run === 'number' ? run : run.Id;
    return this.http
      .post<any>(
        `http://${API_URL}/delete/run`,
        {
          Id: id,
          date: this.dateHandlerService.generateDate(date),
          pipeID: pipeID,
        },
        this.httpOptions
      )
      .pipe(
        tap((_) => console.log('deleted run')),
        catchError(this.handleError<Run>())
      );
  }

  deleteTag(tag: Tag | number): Observable<any> {
    const id = typeof tag === 'number' ? tag : tag.Id;
    return this.http
      .post<any>(`http://${API_URL}/delete/tag`, { Id: id }, this.httpOptions)
      .pipe(
        tap((_) => console.log('deleted tag')),
        catchError(this.handleError<Run>())
      );
  }

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' }),
  };

  createEmptyRun() {
    return {
      Name: '',
      DriverName: '',
      PipeID: '',
      Direction: '',
      Tagged: 0,
      Lat: 0,
      Longi: 0,
      ShowRun: true,
      ShowTag: false,
      tags: [],
    };
  }
}
