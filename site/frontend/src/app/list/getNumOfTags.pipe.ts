import { Pipe, PipeTransform } from '@angular/core';
import { Tag } from '../interfaces';

@Pipe({
  name: 'getNumOfTags',
  pure: true,
})
export class GetNumOfTags implements PipeTransform {
  transform(value: Tag[], args?: any): any {
    return this.getNumOfTags(value);
  }

  getNumOfTags(tags: Tag[]): number {
    if (tags) {
      return tags.length;
    } else {
      return 0;
    }
  }
}
