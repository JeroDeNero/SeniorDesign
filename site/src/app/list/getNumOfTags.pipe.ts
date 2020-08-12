import { Pipe, PipeTransform } from "@angular/core";
import { Tag } from "../run";
import { isNull, isUndefined } from "util";

@Pipe({
    name: 'getNumOfTags',
    pure: true
})

export class GetNumOfTags implements PipeTransform {

    transform(value: Tag[], args?: any): any {
        return this.getNumOfTags(value);
    }

    getNumOfTags(tags: Tag[]): number {
        if (isUndefined(tags)) {
            return 0;
        } else {
            return tags.length;
        }
    }
}