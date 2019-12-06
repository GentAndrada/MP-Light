h = input('Type the initial height in meters: ');
v = input('Magnitude of the velocity in m/s: ');
theta = input('Angle in degrees: ');
ax = input('X-component of the acceleration in m/s^2: ');
ay = input('Y-component of the acceleration in m/s^2: ');

tflight = (2*(v*sind(theta)+h))/-ay;

if ay == 0
    error('Vertical acceleration cannot be 0')
else 
  t = 0:0.01:tflight;
  x = v.*cosd(theta).*t + (ax.*(t).^2)./2;
  y = v.*sind(theta).*t + (ay.*(t).^2)./2 + h;
end

tmax = (v.*sind(theta))./(-ay);
ymax = v.*sind(theta).*tmax + (ay.*(tmax).^2)./2;
total = ymax + h + 10;
plot(x,y,'linewidth',2)
ylim([0 total])
grid; xlabel 'x-coordinate'; ylabel 'y-coordinate'; title 'Projectile Motion'

