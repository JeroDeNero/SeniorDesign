export interface Run {
  Id?: number;
  PipeID: string;
  Direction: string; // does this want to be number or string?
  ShowRun: Boolean;
  ShowTag: Boolean;
  Name?: string;
  DateTaken?: Date;
  DriverName?: string; // does this want to be an enum?
  Lat?: number;
  Longi?: number;
  image?: HTMLImageElement;
  Tagged?: number;
  tags?: Tag[];
}

export interface Tag {
  Id: number;
  Position: number;
  Lat: number;
  Longi: number;
  VideoTime?: number;
}

export interface numHash {
  [index: number]: boolean;
}
