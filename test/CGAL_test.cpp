
#include <CGAL/Exact_predicates_inexact_constructions_kernel.h>
#include <CGAL/Line_2.h>
#include <CGAL/Triangle_2.h>
using namespace std;

typedef CGAL::Exact_predicates_inexact_constructions_kernel K;
typedef K::Point_2 Point_2;
typedef K::Point_3 Point_3;
typedef K::Vector_2 Vector_2;
typedef K::Vector_3 Vector_3;
typedef K::Line_2 Line_2;
typedef K::Triangle_2 Triangle_2;
typedef K::Sphere_3 Sphere_3;
typedef K::Aff_transformation_2 Aff_transformation_2;  
typedef K::Direction_2 Direction_2; 

void test_on_cgal()
{
    Point_2 p1(0.0,0.0), p2(1.0,0.0); //定义两个二维点
    Vector_2 v1(1.0,1.0), v2(1.0,0.0); //定义两个二维向量
    std::cout<<p1<<std::endl;
    std::cout<<p2<<std::endl;

    std::cout<<v1<<std::endl;
    std::cout<<v2<<std::endl;
    
    Point_2  p3 = p1 + v1;
    Vector_2 v3 = p2 - p1;

    std::cout<<p3<<std::endl;
    std::cout<<v3<<std::endl;
    std::cout<<v3*v2<<std::endl;
}

void test_on_cgal2()
{
  Point_3 p1(0.0,0.0,0.0),p2(1.0,0.0,0.0),p3(0.0,1.0,0.0),p4(0.0,0.0,1.0);
  double v;
  v=(1.0/6.0)*(p1[0]*p2[1]*p3[2]+p1[0]*p4[1]*p2[2]+p1[0]*p3[1]*p4[2]-p1[0]*p4[1]*p3[2]-p1[0]*p3[1]*p2[2]-p1[0]*p2[1]*p4[2]-p2[0]*p1[1]*p3[2]-p4[0]*p1[1]*p2[2]-p3[0]*p1[1]*p4[2]+p4[0]*p1[1]*p3[2]+p3[0]*p1[1]*p2[2]+p2[0]*p1[1]*p4[2]+p2[0]*p3[1]*p1[2]+p4[0]*p2[1]*p1[2]+p3[0]*p4[1]*p1[2]-p4[0]*p3[1]*p1[2]-p3[0]*p2[1]*p1[2]-p2[0]*p4[1]*p1[2]-p2[0]*p3[1]*p4[2]-p4[0]*p2[1]*p3[2]-p3[0]*p4[1]*p2[2]+p4[0]*p3[1]*p2[2]+p3[0]*p2[1]*p4[2]+p2[0]*p4[1]*p3[2]);
  std::cout<<abs(v)<<std::endl;
}

void test_on_line()
{


  Point_2 p1(2.0,0.0),p2(0.0,2.0);
  Line_2 l(p1,p2);
  std::cout << l <<std::endl; 
   
  Point_2 p3(0.0,0.0);
  Triangle_2 t(p1,p2,p3);
  std::cout <<t <<std::endl;
  return ;
}

void test_on_sphere()
{
    Point_3 p(0.0,0.0,0.0);
    double r=2;
    Sphere_3 s(p,r);
    std::cout << s <<std::endl;
}

void test_on_aff()
{
}
int main()
{
    test_on_cgal();
    test_on_cgal2();
    test_on_line();
    test_on_sphere();
    test_on_aff();
    return 0;
}
