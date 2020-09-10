import { TestBed } from '@angular/core/testing';

import { sortService } from './array-manipulation.service';

describe('sortService', () => {
  let service: sortService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(sortService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
