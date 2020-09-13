import { Component, OnInit, Injectable } from '@angular/core';
import { RunService } from '../run.service';
import { SortService } from '../sortService.service';
import { Run } from '../interfaces';

@Injectable({
  providedIn: 'root',
})
@Component({
  selector: 'app-side-menu',
  templateUrl: './side-menu.component.html',
  styleUrls: ['./side-menu.component.css'],
})
export class SideMenuComponent implements OnInit {
  allRuns: Run[][];
  runTemp: Run;

  constructor(
    private runService: RunService,
    private sortService: SortService
  ) {}

  ngOnInit(): void {
    this.getRuns();
  }

  getRuns() {
    this.runService.getRuns().subscribe((runs) => (this.allRuns = runs));
  }

  sort(column: any, desc: boolean) {
    typeof this.runTemp[column] === 'string'
      ? this.sortService.sortString(this.allRuns, column, desc)
      : this.sortService.sortNoneString(this.allRuns, column, desc);
  }
}
