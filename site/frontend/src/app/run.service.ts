import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable, of } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';

import { Run } from './interfaces';

import { API_URL } from './env';

@Injectable({
  providedIn: 'root',
})
export class RunService {
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

  constructor(private http: HttpClient) {}

  getRuns(): Observable<Run[][]> {
    return this.http.get<Run[][]>(`${API_URL}/run/getRuns`).pipe(
      tap((_) => console.log('fetched runs')),
      catchError(this.handleError<Run[][]>([]))
    );
  }

  getRun(id: number): Observable<Run> {
    return this.http
      .post<Run>(`${API_URL}/run/getRun`, { id: id }, this.httpOptions)
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

  addRun(run: Run): Observable<Run> {
    return this.http.post<Run>(`${API_URL}`, run, this.httpOptions).pipe(
      tap(() => console.log('added run w/ id={newRun.Id}')),
      catchError(this.handleError<Run>())
    );
  }

  updateRun(run: Run): Observable<any> {
    return this.http.post(`${API_URL}`, run, this.httpOptions).pipe(
      tap((_) => console.log('updated run id =${run.Id}')),
      catchError(this.handleError<any>())
    );
  }

  deleteRun(run: Run | number) {
    const id = typeof run === 'number' ? run : run.Id;
    const url = `${API_URL}/${id}`;

    return this.http.post(url, { Id: id }, this.httpOptions).pipe(
      tap((_) => console.log('seleted hero id=${id}')),
      catchError(this.handleError<Run>())
    );
  }

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' }),
  };
}
