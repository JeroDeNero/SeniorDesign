import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class DateHandlerService {
  constructor() {}

  private DaysEnum = Object.freeze({
    jan: '01',
    feb: '02',
    mar: '03',
    apr: '04',
    may: '05',
    june: '06',
    july: '07',
    aug: '08',
    sept: '09',
    oct: '10',
    nov: '11',
    dec: '12',
  });

  generateDate(fullDate: Date): String {
    const date = String(fullDate).match(
      /\d\d.[a-zA-Z]+.\d\d\d\d.\d\d:\d\d:\d\d/
    )[0];

    const data = date.split(' ');
    const day = data[0];
    const month = this.DaysEnum[data[1].toLocaleLowerCase()];
    const year = data[2];
    const time = data[3];

    return `${year}-${month}-${day}_${time}`;
  }
}
