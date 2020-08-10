export interface Run {
    videoID: number;
    name: string;
    driver: string; // does this want to be an enum?
    pipeID: string;
    direction: string; // does this want to be number or string?
    lat: number;
    long: number;
}
