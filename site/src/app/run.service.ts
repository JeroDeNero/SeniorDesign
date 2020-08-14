import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'

import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';

import { Run } from './interfaces';
import { RUNS } from './mock-run';

@Injectable({
  providedIn: 'root'
})

export class RunService {

  private RunsUrl = 'api/runs'

  /**
 * Handle Http operation that failed.
 * Let the app continue.
 * @param operation - name of the operation that failed
 * @param result - optional value to return as the observable result
 */
  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      console.log(error);

      return of(result as T);
    }
  }

  constructor(
    private http: HttpClient
  ) { }

  getRuns(): Observable<Run[][]> {
    return this.http.get<Run[][]>(this.RunsUrl)
      .pipe(
        tap(_ => console.log('fetched runs')),
        catchError(this.handleError<Run[][]>('this.getRuns', []))
      );
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

  addRun(run: Run): Observable<Run> {
    return this.http.post<Run>(this.RunsUrl, run, this.httpOptions).pipe(
      tap((newRun: Run) => console.log('added run w/ id={newRun.videoID}')),
      catchError(this.handleError<Run>('addHero'))
    );
  }

  updateRun(run: Run): Observable<any> {
    return this.http.put(this.RunsUrl, run, this.httpOptions).pipe(
      tap(_ => console.log('updated run id =${run.videoID}')),
      catchError(this.handleError<any>('updateHero'))
    );
  }

  deleteRun(run: Run | number): Observable<Run> {
    const id = (typeof run === 'number') ? run : run.videoID;
    const url = `${this.RunsUrl}/${id}`;

    return this.http.delete<Run>(url, this.httpOptions).pipe(
      tap(_ => console.log('seleted hero id=${id}')),
      catchError(this.handleError<Run>('deleteRun'))
    );
  }

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };
}
