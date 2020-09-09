import { Component, OnInit } from '@angular/core';
import { RunService } from '../run.service';
import { Run } from '../interfaces';

@Component({
  selector: 'app-side-menu',
  templateUrl: './side-menu.component.html',
  styleUrls: ['./side-menu.component.css'],
})
export class SideMenuComponent implements OnInit {
  allRuns: Run[][];

  constructor(private runService: RunService) {}

  ngOnInit(): void {
    this.runService.getRuns().subscribe((runs) => (this.allRuns = runs));
  }

  getRuns() {
    this.runService.getRuns().subscribe((runs) => (this.allRuns = runs));
  }
}
