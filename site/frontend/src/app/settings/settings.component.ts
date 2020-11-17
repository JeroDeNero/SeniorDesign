import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Observable, of } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';
import { API_URL } from '../env';
import { ToggleService } from '../toggle.service';

@Component({
  selector: 'app-settings',
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css'],
})
export class SettingsComponent implements OnInit {
  wheelRadius: number = 6;
  mainCameraFPS: number = 10;
  backCameraFPS: number = 10;

  constructor(private toggleService: ToggleService, private http: HttpClient) {}

  ngOnInit(): void {
    this.getSettings().subscribe((data) => {
      this.wheelRadius = data['wheelRadius'];
      this.mainCameraFPS = data['mainFPS'];
      this.backCameraFPS = data['secondaryFPS'];
    });
  }

  comfirmBut(wheelRad, mainCamFPS, backCamFPS) {
    const wheel = Number(wheelRad);
    const main = Math.floor(Number(mainCamFPS));
    const back = Math.floor(Number(backCamFPS));

    if (wheel <= 0) {
      alert(`Invalid value for the wheels`);
      return;
    }

    if (main <= 0 && main >= 60) {
      alert(`Invalid value for the front camera's FPS`);
      return;
    }

    if (back <= 0 && back <= 60) {
      alert(`Invalid value for the back camera's FPS`);
      return;
    }

    this.updateSettings(wheel, main, back).subscribe();
  }

  cancelBut() {
    this.toggleService.setShowSettings(false);
  }

  updateSettings(wheelRad, mainCamFPS, backCamFPS): Observable<any> {
    return this.http
      .post(
        `http://${API_URL}/save/settings`,
        { wheelRad: wheelRad, mainCamFPS: mainCamFPS, backCamFPS: backCamFPS },
        this.httpOptions
      )
      .pipe(
        tap((_) => {
          console.log('Updating Settings');
          alert('Updated Settings');
          this.toggleService.setShowSettings(false);
        }),
        catchError(this.handleError<any>())
      );
  }

  getSettings() {
    return this.http.get<any>(`http://${API_URL}/get/settings`).pipe(
      tap(() => console.log('Fetching Settings')),
      catchError(this.handleError<any>(null))
    );
  }

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' }),
  };

  private handleError<T>(result?: T) {
    return (error: any): Observable<T> => {
      console.log(error);

      return of(result as T);
    };
  }
}
