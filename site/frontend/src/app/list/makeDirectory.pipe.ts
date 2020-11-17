import { Pipe, PipeTransform } from '@angular/core';
import { DateHandlerService } from '../date-handler.service';
import { Run } from '../interfaces';

@Pipe({
  name: 'makeDirectory',
  pure: true,
})
export class MakeDirectory implements PipeTransform {
  constructor(private dateHandlerService: DateHandlerService) {}

  transform(run: Run, target: String | '', args?: any) {
    return this.makeDirectory(run.PipeID, run.DateTaken, target);
  }

  makeDirectory(id: string, date: Date, target: String | ''): string {
    return `assets/Data/${id}/${this.dateHandlerService.generateDate(
      date
    )}/${target}`;
  }
}
