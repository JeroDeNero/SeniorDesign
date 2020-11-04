export class Controller {
  public buttons: number[];
  public axes: number[];
  public timestamp: number;

  constructor(controller: Gamepad) {
    this.writeController;
  }

  writeController(controller: Gamepad) {
    this.timestamp = controller.timestamp;

    if (controller.axes.length === 8) {
      this.ps4ToStandard(controller);
    } else if (controller.axes.length === 6) {
      this.oldPSToStandard(controller);
    } else if (
      controller.axes.length === 4 ||
      controller.mapping === 'standard'
    ) {
      this.commonToStandard(controller);
    } else {
      console.log('This controller does not seem to be supported.');
    }
  }

  updateController(controller: Gamepad) {
    this.timestamp = controller.timestamp;

    this.emptyArrays();

    this.writeController(controller);
  }

  emptyArrays() {
    this.buttons = [];
    this.axes = [];
  }

  ps4ToStandard(controller: Gamepad) {
    this.buttons.push(controller.buttons[0].value);
    this.buttons.push(controller.buttons[1].value);
    this.buttons.push(controller.buttons[3].value);
    this.buttons.push(controller.buttons[2].value);
    this.buttons.push(controller.buttons[4].value);
    this.buttons.push(controller.buttons[5].value);
    this.buttons.push((controller.axes[2].valueOf() + 1) / 2);
    this.buttons.push((controller.axes[5].valueOf() + 1) / 2);
    this.buttons.push(controller.buttons[8].value);
    this.buttons.push(controller.buttons[9].value);
    this.buttons.push(controller.buttons[11].value);
    this.buttons.push(controller.buttons[12].value);
    this.buttons.push(Math.max(0, controller.axes[6].valueOf()));
    this.buttons.push(Math.max(0, -1 * controller.axes[6].valueOf()));
    this.buttons.push(Math.max(0, controller.axes[7].valueOf()));
    this.buttons.push(Math.max(0, -1 * controller.axes[7].valueOf()));
    this.buttons.push(controller.buttons[10].value);

    this.axes.push(controller.axes[0].valueOf());
    this.axes.push(controller.axes[0].valueOf());
    this.axes.push(controller.axes[3].valueOf());
    this.axes.push(controller.axes[4].valueOf());
  }

  oldPSToStandard(controller: Gamepad) {
    this.buttons.push(controller.buttons[0].value);
    this.buttons.push(controller.buttons[1].value);
    this.buttons.push(controller.buttons[3].value);
    this.buttons.push(controller.buttons[2].value);
    this.buttons.push(controller.buttons[4].value);
    this.buttons.push(controller.buttons[5].value);
    this.buttons.push((controller.axes[2].valueOf() + 1) / 2);
    this.buttons.push((controller.axes[5].valueOf() + 1) / 2);
    this.buttons.push(controller.buttons[8].value);
    this.buttons.push(controller.buttons[9].value);
    this.buttons.push(controller.buttons[11].value);
    this.buttons.push(controller.buttons[12].value);
    this.buttons.push(controller.buttons[13].value);
    this.buttons.push(controller.buttons[14].value);
    this.buttons.push(controller.buttons[15].value);
    this.buttons.push(controller.buttons[16].value);
    this.buttons.push(controller.buttons[10].value);

    this.axes.push(controller.axes[0].valueOf());
    this.axes.push(controller.axes[0].valueOf());
    this.axes.push(controller.axes[3].valueOf());
    this.axes.push(controller.axes[4].valueOf());
  }

  commonToStandard(controller: Gamepad) {
    this.buttons.push(controller.buttons[0].value);
    this.buttons.push(controller.buttons[1].value);
    this.buttons.push(controller.buttons[2].value);
    this.buttons.push(controller.buttons[3].value);
    this.buttons.push(controller.buttons[4].value);
    this.buttons.push(controller.buttons[5].value);
    this.buttons.push(controller.buttons[6].value);
    this.buttons.push(controller.buttons[7].value);
    this.buttons.push(controller.buttons[8].value);
    this.buttons.push(controller.buttons[9].value);
    this.buttons.push(controller.buttons[10].value);
    this.buttons.push(controller.buttons[11].value);
    this.buttons.push(controller.buttons[12].value);
    this.buttons.push(controller.buttons[13].value);
    this.buttons.push(controller.buttons[14].value);
    this.buttons.push(controller.buttons[15].value);
    this.buttons.push(controller.buttons[16].value);

    this.axes.push(controller.axes[0].valueOf());
    this.axes.push(controller.axes[1].valueOf());
    this.axes.push(controller.axes[2].valueOf());
    this.axes.push(controller.axes[3].valueOf());
  }
}
