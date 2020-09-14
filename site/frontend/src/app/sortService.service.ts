import { Injectable } from '@angular/core';
import { Run } from './interfaces';
import { isArray } from 'util';

@Injectable({
  providedIn: 'root',
})
export class SortService {
  constructor() {}

  sortString(list: any[][] | any[], item, desc: boolean) {
    const lambda = (element: Run, element2: Run) => {
      const target = {
        a: (element[item] || '').toUpperCase(),
        b: (element2[item] || '').toUpperCase(),
      };
      return this.compare(this.valueSwap(target, desc));
    };

    isArray(list[0]) ? this.apply2d(list, lambda) : this.apply1d(list, lambda);
  }

  sortNoneString(list: any[][] | any[], item, desc: boolean) {
    const lambda = (element: any, element2: any) => {
      const target = {
        a: element[item] || '',
        b: element2[item] || '',
      };
      return this.compare(this.valueSwap(target, desc));
    };

    isArray(list[0]) ? this.apply2d(list, lambda) : this.apply1d(list, lambda);
  }

  compare(target) {
    if (target['a'] < target['b']) {
      return -1;
    } else if (target['a'] > target['b']) {
      return 1;
    } else {
      return 0;
    }
  }

  valueSwap(target, desc) {
    return desc ? target : { a: target['b'], b: target['a'] };
  }

  apply2d(list: any[][], lambda) {
    list.forEach((elements: any[]) => {
      elements.sort(lambda);
    });
  }

  apply1d(list: any[], lambda) {
    return list.forEach((elements: Run[]) => {
      elements.sort(lambda);
    });
  }
}
